# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class WuhanspiderSpider(scrapy.Spider):
    name = 'wuHanSpider'
    allowed_domains = ['tianqi.com']
    citys = ['wuhan', 'shanghai']
    start_urls = []
    for city in citys:
        start_urls.append('https://www.tianqi.com/' + city)

    def parse(self, response):
        items= []
        city = response.xpath('//dd[@class="name"]/h2/text()').extract()
        Selector = response.xpath('//div[@class="day7"]')
        date = Selector.xpath('ul[@class="week"]/li/b/text()').extract()
        week = Selector.xpath('ul[@class="week"]/li/span/text()').extract()
        wind = Selector.xpath('ul[@class="txt"]/li/text()').extract() 
        weather = Selector.xpath('ul[@class="txt txt2"]/li/text()').extract()
        temperature1 = Selector.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()
        temperature2 = Selector.xpath('div[@class="zxt_shuju"]/ul/li/b/text()').extract()
        for i in range(7):
            item = WeatherItem()
            try:
                item['cityDate'] = city[0] + date[i]
                item['week'] = week[i]
                item['wind'] = wind[i]
                item['temperature'] = temperature1[i] + ',' + temperature2[i]
                item['weather'] = weather[i]
            except IndexError as e:
                sys.exit(-1)
            items.append(item)
        return items
