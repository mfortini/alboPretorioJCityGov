import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from alboPretorioJCityGov.items import AlbopretorioJCityGovItem, AlbopretorioJCityGovPDF

import re

link_dettaglio_re=re.compile(re.compile('(http.*?);'))

from ConfigParser import ConfigParser

cp=ConfigParser()
cp.read('alboPretorio.cfg')

ALBO_BASE_URL=cp.get('settings','ALBO_BASE_URL')

class alboPretorioSpider(Spider):
    name = "alboPretorio"
    start_urls= [
		ALBO_BASE_URL,
            ]

    def parse(self, response):
        sel = Selector(response)
        table = sel.xpath('//table')
        rows = table.xpath('.//tr')
        items = []
	self.logger.info("Found %d rows" % (len(rows),))
        for row in rows:
            item = AlbopretorioJCityGovItem()
            #tipo_documento  = Field()
            #documenti       = Field()
            try:
		(id_registro_anno,id_registro_num) =row.xpath('.//td[@class="annonumeroregistrazione number"]/text()').extract()[0].split('/')
		#annonum         =row.xpath('.//td[2]/text()').extract().trim()
		try:
			tipo_atto       =row.xpath('.//td[@class="categoria text"]/text()').extract()[0].strip()
		except IndexError:
			tipo_atto = ''
		oggetto         =row.xpath('.//td[@class="oggetto text"]/text()').extract()[0].strip()
		(data_inizio_pub,data_fine_pub)     =row.xpath('.//td[@class="periodo-pubblicazione date"]/text()').extract()
		link_dettaglio =row.xpath('.//td[@class="actions"]').xpath('.//a[i[@class="icon-detail"]]/@href').extract()[0]


		item['id_registro_anno']=id_registro_anno.strip()
		item['id_registro_num']=id_registro_num.strip()
		item['tipo_atto']=tipo_atto.strip()
		item['oggetto']=oggetto.strip()
		item['data_inizio_pub']=data_inizio_pub.strip()
		item['data_fine_pub']=data_fine_pub.strip()
		item['link_dettaglio']=link_dettaglio_re.match(link_dettaglio).group(1)

                items.append(item)
            except IndexError:
                pass


        return items

