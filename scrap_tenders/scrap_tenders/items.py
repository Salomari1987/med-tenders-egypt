# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# from scrapy.item import Item, Field
#
#
# class StackItem(Item):
#     Tender_Notice_Type = Field()
#     Country = Field()
#     Category = Field()
#     Description = Field()
#     Deadline = Field()
#     Ref = Field()


from scrapy_djangoitem import DjangoItem
from tenders_django_app.models import Tender

class StackItem(DjangoItem):
    django_model = Tender
