# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    rating = scrapy.Field()
    review_text = scrapy.Field()
    pass

    # define the fields for your item here like:
    # name = scrapy.Field()
