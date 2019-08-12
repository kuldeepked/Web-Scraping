# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        h1_tag = response.xpath("//h1/a/text()").extract()
        tag = response.xpath("//*[@class ='tag-item']/a/text()").extract()

        yield{
            'h1': h1_tag,
            'tags': tag,
        }
