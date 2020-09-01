# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import codecs

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        with codecs.open(fileName, 'a', 'utf-8') as fp:
            fp.write("%s \t %s \t %s \t %s \t %s \r\n" 
                    %(item['cityDate'],
                        item['week'],
                        item['temperature'],
                        item['weather'],
                        item['wind']))
        return item
