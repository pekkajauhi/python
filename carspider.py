# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
url_short = 'https://www.nettiauto.com'
basic_url = 'https://www.nettiauto.com/vaihtoautot?page='
urls = [basic_url+str(x+1) for x in range(1000)]

class CarspiderSpider(scrapy.Spider):
	name = 'carspider'
	allowed_domains = ['www.nettiauto.com']
	start_urls = ['http://www.nettiauto.com/']
	def start_requests(self):
		yield scrapy.Request(url = url_short, callback = self.parse_front)

	def parse_front(self, response):
		for url in urls:
			yield response.follow(url=url, callback = self.parse1)
			
	def parse1(self, response):
		car_urls = response.xpath('//div[@class="listing_thumb"]/a/@href').extract()[:30]
		for url in car_urls:
			yield response.follow(url=url, callback = self.parse2)
			
	def parse2(self, response):

		
		make = response.css('h1 > a > span::text').extract_first()
		model = response.css('div.lnh22 > h1 > a > span > span::text').extract_first()
		vm = response.css('td.bold::text').extract_first()
		km = response.xpath('//td[contains(.,"km")]/text()').extract_first()
		motor = response.xpath('//td[contains(.,"l,")]/text()').extract_first()
		gear = response.xpath('//td[contains(.,"Vaihteisto")]/following-sibling::td[contains(@class,"bold")]/text()').extract_first()
		power = response.xpath('//div[contains(@class,"acc_det")]/div/b[text()[contains(.,"kW")]]/text()').extract_first()
		top_speed = response.xpath('//*[text()[contains(.,"km/h")]]/text()').extract_first()
		accel = response.xpath('//div[contains(.,"Kiihtyvyys")]/child::b/text()').extract_first()
		mileage = response.css('div.acc_det > div > b:nth_child(6)::text').extract_first()
		mass = response.xpath('//b[text()[contains(.,"kg")]]/text()').extract_first()
		price = response.xpath('//span[contains(@class,"small_text18")]/span/text()').extract_first()

		
		car_list = [make,model,vm,km,motor,gear,power,top_speed,accel,mileage,mass,price]
		ultimate_list.append(car_list)
		
		asd = {'asd':ultimate_list}
		if len(ultimate_list) > 29900:
			df = pd.DataFrame(ultimate_list, columns=['Merkki','Malli','Vuosimalli','Mittarilukema','Moottori','Vaihteisto',
			'Teho','Huippunopeus', 'Kiihtyvyys','Kulutus/yhdistetty','Omamassa','Hinta'])
			df.to_excel("cars_data_3000.xlsx")
			yield asd
		
		
ultimate_list = []
