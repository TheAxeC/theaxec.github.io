module Jekyll

	class CategoryIndex < Page    
		def initialize(site, base, dir, tag)
			@site = site
			@base = base
			@dir = dir
			@name = 'index.html'

			self.process(@name)
			self.read_yaml(File.join(base, '_layouts'), 'cat_index.html')
			self.data['category'] = tag
		end
	end

	class CategoryGenerator < Generator
		safe true
	
		def generate(site)
			if site.layouts.key? 'cat_index'
				dir = 'category'
				site.categories.keys.each do |category|
					write_cat_index(site, File.join(dir, category), category)
				end
			end
		end
	
		def write_cat_index(site, dir, category)
			index = CategoryIndex.new(site, site.source, dir, category)
			index.render(site.layouts, site.site_payload)
			index.write(site.dest)
			site.pages << index
		end
	end
end