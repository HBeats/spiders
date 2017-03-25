import scrapy
import saves

class PublisherSpider(scrapy.Spider):
	name = "publishers"
	start_urls = ["https://www.fakku.net/hentai/publishers"]

	def parse(self, response):

		#save file
		filename = "f-publisher.html"
		saves.save_file(response.body, filename)

		href = response.css("a.attribute-row::attr(href)").extract()
		for link in href:
			yield scrapy.Request(response.urljoin(link), callback = self.parse_pub)

	def parse_pub(self, response):
		def extract_with_css(query):
			return response.css(query).extract_first().strip()

		name = extract_with_css("h1.attribute-title::text").replace("Hentai", "").strip()
		#Saving the file
		filename = "publisher-{}.html".format(name.lower().replace(" ", "-"))
		saves.save_file(response.body, filename)

		yield {
			"name": name,
			"followers": extract_with_css("div.attribute-subscribers span::text")
		}