# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityDate = scrapy.Field() #城市及日期
    week = scrapy.Field() #星期
    temperature = scrapy.Field() #温度
    weather = scrapy.Field() #天气
    wind = scrapy.Field() #风力
