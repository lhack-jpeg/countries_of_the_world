import scrapy

def country(response, value):
	return response.xpath('//div[@class="country-info"]/span[@class="' + value +'"]/text()').extract()

class WorldDataSpider(scrapy.Spider):
    name = 'world_data'
    allowed_domains = ['scrapethissite.com/pages']
    start_urls = ['https://scrapethissite.com/pages/simple/']

    def parse(self, response):
        names = response.xpath('//h3[@class="country-name"]/text()').extract()
        for name in names:
        	name = name.replace("\n","")
        capital = country(response, 'country-capital')
        population = country(response, 'country-population')
        area = country(response, 'country-area')
        yield{
        	"Name" : name,
        	"Capital city" : capital,
        	"Population" : population,
        	"Area (km^2)" : area
        }
