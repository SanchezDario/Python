from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader

class Sacando(Field):
    inicio = Field()
    minimo = Field()

class Pagina(Spider):
    name = "laPagina"
    url = ['https://www.coingecko.com']


