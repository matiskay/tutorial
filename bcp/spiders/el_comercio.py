from scrapy import Spider
from w3lib.html import remove_tags, remove_tags_with_content
from bcp.items import BcpItem



class ElComercio(Spider):
    name = 'el_comercio'
    start_urls = [
            'https://elcomercio.pe/politica/frente-amplio-anuncia-nueva-denuncia-constitucional-pedro-chavarry-noticia-nndc-611514',
            'https://elcomercio.pe/deporte-total/futbol-peruano/seleccion-peruana-perdio-oportunidad-jugar-campeon-mundo-noticia-611606',
            'https://elcomercio.pe/peru/lista-carreteras-pais-afectadas-debido-intensas-lluvias-noticia-nndc-611444'
            ]
    
    def parse(self, response):
        item = BcpItem()

        title = response.xpath('//h1/text()').extract_first(default='')

        content = response.xpath('//div[has-class("news-text-content")]/p').extract()
        content = '\n'.join(content)
        content = remove_tags(content)

        image = response.xpath('//div[has-class("image")]//img/@src').extract_first()

        item['title'] = title
        item['content'] = content
        item['image'] = image
        item['url'] = response.url

        yield item
