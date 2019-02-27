from scrapy import Spider
from bcp.items import NewsItemLoader



class ElComercio(Spider):
    name = 'el_comercio'
    start_urls = [
            'https://elcomercio.pe/politica/frente-amplio-anuncia-nueva-denuncia-constitucional-pedro-chavarry-noticia-nndc-611514',
            'https://elcomercio.pe/deporte-total/futbol-peruano/seleccion-peruana-perdio-oportunidad-jugar-campeon-mundo-noticia-611606',
            'https://elcomercio.pe/peru/lista-carreteras-pais-afectadas-debido-intensas-lluvias-noticia-nndc-611444'
            ]
    
    def parse(self, response):
        nl = NewsItemLoader(response=response)

        nl.add_xpath('title', '//h1')
        nl.add_xpath('content', '//div[has-class("news-text-content")]/p')
        nl.add_xpath('image', '//div[has-class("image")]//img/@src')
        nl.add_value('url', response.url)

        yield nl.load_item()
