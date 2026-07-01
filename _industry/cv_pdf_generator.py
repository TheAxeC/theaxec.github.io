"""
Industry-focused CV + cover letter generator.

Reuses the Awesome-CV templating engine from ../_scripts/cv_pdf_generator.py
(the `Template` class) and the same src/-templates -> _tmp/ -> xelatex pipeline,
but renders an INDUSTRY-tailored CV instead of the academic one.

A single data file (../_data/industry.yml) holds shared personal info plus one
block per *profile*. Switch profile with --profile:

    python cv_pdf_generator.py --profile analyst   # Senior Data Analyst (Guerrilla Games)
    python cv_pdf_generator.py --profile pharma    # Biomedical / pharma data science

By default both the CV and (if the profile defines one) the cover letter are
generated and compiled. Use --save to copy the resulting PDFs to the repo root
as cv-industry-<profile>.pdf / coverletter-<profile>.pdf.
"""

import argparse
import os
import sys
import shutil
import errno
import subprocess

import yaml

# Reuse the exact templating engine the academic CV uses.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_scripts"))
from cv_pdf_generator import Template  # noqa: E402


class IndustryGenerate:
    def __init__(self, src, dst, data_file, profile, latex, quiet=False, compact=False):
        self.src = src
        self.dst = dst
        self.data_file = data_file
        self.profile = profile
        self.latex = latex
        self.quiet = quiet
        self.compact = compact
        self.context = {}

    # --- context -------------------------------------------------------------
    def computeContext(self):
        with open(self.data_file, "r") as stream:
            raw = yaml.safe_load(stream)

        if self.profile not in raw["profiles"]:
            available = ", ".join(raw["profiles"].keys())
            raise SystemExit(
                f"Unknown profile '{self.profile}'. Available: {available}"
            )

        shared = raw.get("shared", {})
        prof = raw["profiles"][self.profile]

        personal = dict(shared.get("personal", {}))
        personal["titles"] = prof.get("titles", personal.get("titles", []))
        personal["photo_loc"] = "../../"

        data = {"personal": personal}
        for key in ("summary", "skills", "experience", "projects", "education", "teaching", "awards"):
            if key in prof:
                data[key] = prof[key]

        self.context = {
            "data": data,
            "letter": prof.get("letter"),
            "profile": self.profile,
            "compact": self.compact,
        }

    # --- file plumbing (mirrors the academic generator) ----------------------
    def mkdir(self, path):
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

    def copyFiles(self):
        """Copy everything that is not a template (cls, fonts) into _tmp."""
        try:
            shutil.rmtree(self.dst)
        except OSError:
            pass
        for root, _dirs, filenames in os.walk(self.src):
            for filename in filenames:
                if filename.endswith(".template"):
                    continue
                orig = os.path.join(root, filename)
                new = orig.replace(self.src, self.dst)
                self.mkdir(new)
                shutil.copy(orig, new)

    def parseTemplate(self, filename):
        with open(filename) as stream:
            template = stream.read()
        output = Template(template).render(False, self.context)
        out_file = filename.replace(self.src, self.dst).replace(".template", "")
        self.mkdir(out_file)
        with open(out_file, "w") as fh:
            fh.write(output)

    def retrieveTemplates(self):
        for root, _dirs, filenames in os.walk(self.src):
            for filename in filenames:
                if not filename.endswith(".template"):
                    continue
                # The cover letter template is only rendered if data exists.
                if filename.startswith("coverletter") and not self.context.get("letter"):
                    continue
                self.parseTemplate(os.path.join(root, filename))

    def generate(self):
        self.copyFiles()
        self.computeContext()
        self.retrieveTemplates()

    # --- compilation ---------------------------------------------------------
    def compileOne(self, main_file):
        saved = os.getcwd()
        os.chdir(self.dst)
        cmd = [self.latex, main_file, f"-output-directory={saved}"]
        print("Running:", " ".join([self.latex, main_file]))
        try:
            if self.quiet:
                subprocess.run(cmd, stdout=subprocess.DEVNULL)
            else:
                subprocess.run(cmd)
        except FileNotFoundError:
            print(f"Error: {self.latex} not found in PATH")
        for ext in ["aux", "log", "out", "fls", "fdb_latexmk"]:
            f = main_file.replace("tex", ext)
            if os.path.isfile(f):
                os.remove(f)
        os.chdir(saved)

    def compileLatex(self):
        self.compileOne("cv.tex")
        if self.context.get("letter") and os.path.isfile(
            os.path.join(self.dst, "coverletter.tex")
        ):
            self.compileOne("coverletter.tex")

    def savePDF(self):
        if self.compact:
            # One-page variant: save only the CV, with a suffix, so the full
            # CV and the (already one-page) cover letter are not overwritten.
            mapping = {"cv.pdf": f"../cv-industry-{self.profile}-onepage.pdf"}
        else:
            mapping = {
                "cv.pdf": f"../cv-industry-{self.profile}.pdf",
                "coverletter.pdf": f"../coverletter-{self.profile}.pdf",
            }
        for src_name, dest in mapping.items():
            src_path = os.path.join(self.dst, src_name)
            if os.path.isfile(src_path):
                shutil.copy(src_path, dest)
                print("Saved", dest)

    def run(self):
        self.generate()
        self.compileLatex()


def main():
    parser = argparse.ArgumentParser(
        description="Generate an industry-focused CV + cover letter (Awesome-CV).",
    )
    parser.add_argument(
        "--profile",
        default="analyst",
        help="Which profile to render (analyst | pharma | ...). Default: analyst.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="Generate + compile (default).")
    group.add_argument("--templates", action="store_true", help="Only render .tex (no compile).")
    parser.add_argument("--quiet", action="store_true", help="Suppress LaTeX logs.")
    parser.add_argument("--save", action="store_true", help="Copy PDFs to the repo root.")
    parser.add_argument(
        "--compact",
        action="store_true",
        help="One-page CV: drop items marked 'compact: false' and tighten spacing.",
    )
    args = parser.parse_args()

    os.chdir(os.path.dirname(__file__))
    engine = IndustryGenerate(
        src="./src/",
        dst="./_tmp/",
        data_file="../_data/industry.yml",
        profile=args.profile,
        latex="xelatex",
        quiet=args.quiet,
        compact=args.compact,
    )

    if args.templates:
        engine.generate()
    else:
        engine.run()
    if args.save:
        engine.savePDF()


if __name__ == "__main__":
    main()
