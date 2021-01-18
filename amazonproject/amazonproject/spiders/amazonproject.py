# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem
from scrapy.loader import ItemLoader



class AmazonCrawlerSpider(scrapy.Spider):
    name = 'amazonproject'
    start_urls = ['https://www.amazon.co.uk/Perfecting-Exfoliant-Breakouts-Blackheads-Enlarged/product-reviews/B07C5SS6YD/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']
    allowed_domains = ["amazon.co.uk"]


    def parse(self, response):
        reviews = response.xpath("//div[@class='a-section celwidget']")
        for review in reviews:
            loader = ItemLoader(item=AmazonItem(), selector=review, response=response)
            loader.add_xpath("name", ".//span[@class='a-profile-name']/text()")
            loader.add_xpath("rating", ".//span[@class='a-icon-alt']/text()")
            loader.add_xpath("review_text", ".//span[@class='a-size-base review-text review-text-content']/span/text()")
            yield loader.load_item()


        next_page = response.xpath("//li[@class='a-last']/a/@href").get()
        if next_page:
            absolute_url = f'https://amazon.co.uk{next_page}'
            yield scrapy.Request(
                url=absolute_url,
                callback=self.parse
            )


          
