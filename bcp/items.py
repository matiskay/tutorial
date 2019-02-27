# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

from w3lib.html import remove_tags


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()


class NewsItemLoader(ItemLoader):
    default_item_class = NewsItem

    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(remove_tags, str.strip)

    content_out = Join('\n')
