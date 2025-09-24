import argparse
import re
import os
import shutil
import yaml
import errno
import datetime
import subprocess

# TEMPLITE : http://code.activestate.com/recipes/496702/
class Template():
    def __init__(self, text):
        self.delimiter = re.compile(r'{%(.*?)%}', re.DOTALL)
        self.tokens = self.compile(text)

    def compile(self, text):
        tokens = []
        for index, token in enumerate(self.delimiter.split(text)):
            if index % 2 == 0:
                # plain string
                if token: tokens.append((False, token.replace('%\\}', '%}').replace('{\\%', '{%')))
            else:
                # code block
                # find out the indentation
                lines = token.replace('{\\%', '{%').replace('%\\}', '%}').splitlines()
                indent = min([len(l) - len(l.lstrip()) for l in lines if l.strip()])
                realigned = '\n'.join(l[indent:] for l in lines)
                tokens.append((True, compile(realigned, '<tempalte> %s' % realigned[:20], 'exec')))
        return tokens

    def tex_escape(self, text):
        """
            :param text: a plain text message
            :return: the message escaped to appear correctly in LaTeX
        """
        text = str(text)
        conv = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
            '<': r'\textless ',
            '>': r'\textgreater ',
        }
        regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
        return regex.sub(lambda match: conv[match.group()], text)

    def to_date(self, text):
        date = datetime.datetime.strptime(str(text), "%Y-%m-%d %H:%M:%S%z")
        return date.strftime("%b. %Y")

    def to_specific_date(self, text):
        date = datetime.datetime.strptime(str(text), "%Y-%m-%d %H:%M:%S%z")
        return date.strftime("%b. %d, %Y")

    def render(self, minimal, context = None, **kw):
        """Render the template according to the given context"""
        global_context = {}
        if context: global_context.update(context)
        if kw: global_context.update(kw)

        # add function for output
        def emit(*args):
            result.extend([self.tex_escape(arg) for arg in args])
        def emit_tex(*args):
            result.extend([str(arg) for arg in args])
        def emit_braces(*args):
            result.extend(["{"+self.tex_escape(arg)+"}" for arg in args])
        def to_date(arg):
             return self.to_date(arg)
        def to_specific_date(arg):
             return self.to_specific_date(arg)
        def fmt_emit(fmt, *args):
            result.append(fmt % args)
        def list_to_string(arg):
            return " and ".join([", ".join(arg[:-1]),arg[-1]] if len(arg) > 2 else arg)
        def check_minimal(arg):
            if not minimal: result.extend(arg)
        def is_minimal():
            return minimal

        global_context['emit'] = emit
        global_context['fmt_emit'] = fmt_emit
        global_context['emit_braces'] = emit_braces
        global_context['emit_tex'] = emit_tex
        global_context['to_date'] = to_date
        global_context['to_specific_date'] = to_specific_date
        global_context['list_to_string'] = list_to_string
        global_context['check_minimal'] = check_minimal
        global_context['is_minimal'] = is_minimal

        # run the code
        result = []
        for is_code, token in self.tokens:
            if is_code: exec(token, global_context)
            else: result.append(token)
        return ''.join(result)

class Generate:
    def __init__(self, src, dst, data_src, minimal, extension, main, latex, quiet=False):
        self.src = src
        self.dst = dst
        self.data_src = data_src
        self.extension = extension
        self.main = main
        self.latex = latex
        self.minimal = minimal
        self.quiet = quiet

    def parseTemplate(self, filename):
        with open(filename) as stream:
            template = stream.read()
        output = Template(template).render(self.minimal, self.context)
        output_file = filename.replace(self.src, self.dst).replace(self.extension, "")
        self.mkdir(output_file)
        with open(output_file, "w") as text_file: text_file.write(output)

    def computeContext(self):
        self.context = {}
        for root, directories, filenames in os.walk(self.data_src):
            for filename in filenames:
                path = os.path.join(root, filename)
                with open(path, 'r') as stram:
                    content = yaml.safe_load(stram)
                key = os.path.splitext(filename)[0]
                self.context[key] = content
        self.context['data']['personal']['photo_loc'] = "../../"

    def retrieveTemplates(self):
        for root, directories, filenames in os.walk(self.src):
            for filename in filenames:
                if filename.endswith(self.extension):
                    path = os.path.join(root, filename)
                    self.parseTemplate(path)

    def mkdir(self, path):
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def copyFile(self, src, dest):
        try:
            shutil.copy(src, dest)
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)

    # copy fixed files from src to dst
    def copyFiles(self):
        try:
            shutil.rmtree(self.dst)
        except IOError as e:
            pass
        for root, directories, filenames in os.walk(self.src):
            for filename in filenames:
                if not filename.endswith(self.extension):
                    orig = os.path.join(root,filename)
                    new = orig.replace(self.src, self.dst)
                    self.mkdir(new)
                    self.copyFile(orig, new)

    def compileLatex(self):
        savedPath = os.getcwd()
        os.chdir(self.dst)
        cmd = [self.latex, self.main, f"-output-directory={savedPath}"]
        print("Running:", " ".join([self.latex, self.main]))
        try:
            if self.quiet:
                # Suppress normal logs, keep errors visible
                subprocess.run(cmd, stdout=subprocess.DEVNULL)
            else:
                subprocess.run(cmd)
        except FileNotFoundError:
            print(f"Error: {self.latex} not found in PATH")
        # clean auxiliary files
        for ext in ["aux", "log", "out", "fls", "fdb_latexmk"]:
            f = self.main.replace("tex", ext)
            if os.path.isfile(f): os.remove(f)
        os.chdir(savedPath)
    
    def savePDF(self):
        try:
            shutil.copy(self.dst + "cv.pdf", "../cv.pdf")
        # eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        # eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)

    def run(self):
        self.generate()
        self.compileLatex()
    
    def generate(self):
        self.copyFiles()
        self.computeContext()
        self.retrieveTemplates()

# main function
def main():
    parser = argparse.ArgumentParser(
        prog="script.py",
        description=(
            "This tool generates LaTeX files from templates and data, "
            "and can optionally compile them using LaTeX."
        ),
        epilog=(
            "Examples:\n"
            "  python script.py --all\n"
            "  python script.py --templates\n"
            "  python script.py --compile\n"
            "  python script.py --all --minimal\n"
            ""
            "Running:\n"
            "  python script.py --save --quiet\n"
            "Will run the entire pipeline and save the resulting\n file to the home folder"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="Run full pipeline (default): copy files, parse data, generate templates, and compile LaTeX.")
    group.add_argument("--templates", action="store_true", help="Only generate templates: copy files, parse data, and render templates (no compilation).")
    group.add_argument("--compile", action="store_true", help="Only compile LaTeX: assumes templates are already generated.")
    parser.add_argument("--minimal", action="store_true", help="Render templates in minimal mode (reduced output, controlled in template logic).")
    parser.add_argument("--quiet", action="store_true", help="Suppress LaTeX compilation logs (errors are still shown).")
    parser.add_argument("--save", action="store_true", help="Save the resulting LaTeX pdf to the home folder.")
    args = parser.parse_args()

    # information about output location for the tex files
    dst = "./_tmp/"
    # information about the location for the template files
    src = "./src/"
    # information about the location for the data files
    data_src = "../_data/"
    # extension used for templates
    extension = ".template"
    # main file
    main_file = "cv.tex"
    # latex command
    latex = "xelatex"
    # minimal
    minimal = args.minimal

    engine = Generate(src, dst, data_src, minimal, extension, main_file, latex, quiet=args.quiet)

    if args.templates:
        engine.generate()
    elif args.compile:
        engine.compileLatex()
    else:  # default or --all
        engine.run()
    if args.save: engine.savePDF()

# entry point
if __name__ == "__main__":
    main()