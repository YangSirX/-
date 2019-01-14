# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem
"""//ul[@class="top-list  fn-clear"]/li/h5/text()"""

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        # print(response.status_code,response.content,response.text)

        # 获取剧集名
        movie_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # print(movie_list)
        # /h5/text()
        for li in movie_list:
            movie_name = li.xpath('h5/a/text()').extract_first()
            movie_status = li.xpath('span/font/text()').extract_first()
            movie_status2 = li.xpath('span/span/em')
            if movie_status2:
                movie_status2 = movie_status2.xpath('text()').extract_first()
            else:
                movie_status2 = '全剧完结'
            movie_cats = li.xpath('span[2]/text()').extract_first()
            movie_address =  li.xpath('span[3]/text()').extract_first()
            update_time = li.xpath('div[@class="lasted-time new100time fn-right"]/text()').extract_first()
            # print(movie_name)
            # print(movie_status)
            # print(movie_status2)
            # print(movie_cats)
            # print(movie_address)
            # print(update_time)
            # print('*' * 40)
            # pass
            item = MovieItem()
            item['name'] = movie_name
            item['status'] = movie_status
            item['status2'] = movie_status2
            item['movie_cats'] = movie_cats
            item['movie_address'] = movie_address
            item['update_time'] = update_time

            yield item
