# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from django.db import IntegrityError
from classifier import classify


class ScrapTendersPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except IntegrityError:
            pass
        return item


class ClassifyTendersPipeline(object):
    def process_item(self, item, spider):
        item['classification'] = classify(item['Description'])
        return item
