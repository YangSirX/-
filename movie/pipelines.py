# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class MoviePipeline(object):
    def process_item(self, item, spider):
        # with open('my_meiju.txt','a',encoding='utf-8') as f:
        #     f.writelines([item['name'] + ' ',item['status'] + ' ',item['status2'] + ' ',item['movie_cats'] + ' ',item['movie_address'] + ' ',item['update_time'] + '\n'] )
        #     # f.write() + '\n')
        # return item
        datas = [item['name'],item['status'],item['status2'],item['movie_cats'],item['movie_address'],item['update_time']]
        with open('testwrite.csv', mode='a', newline='', encoding='utf-8')as f:
            writer = csv.writer(f)
            # for row in datas:
            writer.writerow(datas)
