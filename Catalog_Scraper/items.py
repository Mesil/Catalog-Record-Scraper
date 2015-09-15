# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class catalogscraperItem(scrapy.Item):
	title = scrapy.Field()
	# subject = scrapy.Field(output_processor=Join(', '))
	# description = scrapy.Field()
	# creator = scrapy.Field(output_processor=Join())
	# source = scrapy.Field()
	# published = scrapy.Field()
	# rights = scrapy.Field()
	# citation = scrapy.Field(output_processor=Join())
	# url = scrapy.Field()
	pass
