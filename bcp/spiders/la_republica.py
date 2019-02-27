from scrapy import Spider
from bcp.items import NewsItemLoader


class LaRepublicaSpider(Spider):
    name = 'la_republica'
    start_urls = [
        'https://larepublica.pe/politica/1421312-pedro-chavarry-fiscal-pedir-prision-preventiva-extitular-ministerio-publico-yvan-montoya',
    ]

    def parse(self, response):
        nl = NewsItemLoader(response=response)

        nl.add_xpath('title', '//h1')
        nl.add_xpath('content', '//div[has-class("content-post")]')
        nl.add_xpath('image', '//img[has-class("Img-conver__img")]/@data-original')
        nl.add_value('url', response.url)

        yield nl.load_item()