import scrapy
import saves

#for scraping offline html pages of F! publishers
class PublisherSpider(scrapy.Spider):
	name = "publishers_off"
	path = "file://G:/CompSci/1codingpersonal/python personal/scrapy/f/"
	start_urls = [ path + "f-publisher.html" ]

	def parse(self, response):
		href = response.css("a.attribute-row::attr(href)").extract()
		self.log(href)
		for link in href:
			link = link.replace("/publishers/", "")
			link = self.path + "publisher-" + link + ".html"
			yield scrapy.Request(link, callback = self.parse_pub)

	def parse_pub(self, response):
		def extract_with_css(query):
			return response.css(query).extract_first().strip()

		name = extract_with_css("h1.attribute-title::text").replace("Hentai", "").strip()

		yield {
			"name": name,
			"followers": extract_with_css("div.attribute-subscribers span::text")
		}