# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        title = response.xpath('//div[@class="title_wrapper"]/h1/text()').get()
        year = response.xpath('//span[@id="titleYear"]/a/text()').get()
        duration = response.xpath('//time[@datetime="PT142M"]/text()').get()
        summary = response.xpath('normalize-space(//div[@class="summary_text"]/text())').get()
        yield{
            "Title" : title,
            "Year" : year,
            "Duration" : duration,
            "Short Description" : summary
        }
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
