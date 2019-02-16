# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
url_short = 'https://www.etuovi.com/myytavat-asunnot/'
basic_url = 'https://www.etuovi.com/myytavat-asunnot/?page='
urls = [basic_url+str(i+1) for i in range(5000)]


class JkspiderSpider(scrapy.Spider):
	name = 'jkspider'
	def start_requests(self):
		yield scrapy.Request(url = url_short, callback = self.parse_front)
		
	def parse_front(self, response):		
		for url in urls:
			yield response.follow(url=url, callback = self.parse2)

	def parse2(self, response):
		
		
		sizelist = response.css('a.facts > div > div.size > span::text').extract()
		pricelist = response.css('a.facts > div > div.price > span:first-child::text').extract()
		yearlist = response.css('a.facts > div > div.year').extract()
		typelist = response.css('a.facts > div > div.type > label::text').extract()
		placelist = response.css('a.facts > div > div.address > span::text').extract()
		detailslist = response.css('a.facts > div > div.type > span').extract()
		
		for size in sizelist:
			sizes.append(size)
		for price in pricelist:
			prices.append(price)
		for year in yearlist:
			years.append(year)
		for i in typelist:
			types.append(i)
		for i in placelist:
			places.append(i)
		for i in detailslist:
			details.append(i)


			
		if len(sizes) > 49999:
			ressut['size'] = sizes
			ressut['price'] = prices
			ressut['year'] = years
			ressut['type'] = types
			ressut['place'] = places
			ressut['details'] = details
			res_df = pd.DataFrame.from_dict(ressut)
			res_df.to_excel("output4.xlsx")
			yield ressut
		
ressut = dict()
sizes = []
prices = []
years = []
types = []
places = []
details = []
