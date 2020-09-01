# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import codecs
import json

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.json'
        with codecs.open(fileName, 'a', 'utf-8') as fp:
            jsonStr = json.dumps(dict(item))
            fp.write("%s \r\n" %jsonStr)
        return item
