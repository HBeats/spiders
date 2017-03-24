import scrapy
#A spider to get f tags list
class MALSpider(scrapy.Spider):
	name = "f_tags"
	
	start_urls = ["https://www.fakku.net/tags"]
	
	def parse(self, response):
		filename = "f_tags.html"
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log("Saved file")

		tags = response.css("ul.browse-links li a::attr(title)").extract()
		for tag in tags:
			text = tag
			file = 'f_tags.txt'
			with open(file, 'a') as f:
				f.write(tag + "\n")