# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

from w3lib.html import remove_tags

_clean_spaces_re = re.compile(' +', re.U)


def clean_spaces(value):
    return _clean_spaces_re.sub(' ', value)


def clean_html(html):
    html = html.replace('\xa0', ' ')
    return html

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()


class NewsItemLoader(ItemLoader):
    default_item_class = NewsItem

    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(clean_spaces, clean_html, remove_tags, str.strip)

    content_out = Join('\n')
