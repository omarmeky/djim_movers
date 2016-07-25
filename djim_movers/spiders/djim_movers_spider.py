import scrapy

from djim_movers.items import DjimMoversItem

class DjimMoversSpider(scrapy.Spider):
    name = "djim_movers"
    start_urls = [
        "http://quotes.wsj.com/index/XX/DJIM",
    ]

    def parse(self, response):
        for sel in response.xpath('//table[@id="cr_movers_table"]/tbody/tr[not(th)]'):
            if sel.xpath('.//td[@class="rowTitle"]/h5/a/@href')[0].extract().rfind('/') == 21:
                item = DjimMoversItem()
                item['name'] = sel.xpath('.//td[@class="rowTitle"]/h4/a/text()')[0].extract()
                item['symbol'] = sel.xpath('.//td[@class="rowTitle"]/h5/a/text()')[0].extract()
                item['change'] = sel.xpath('.//td')[2].xpath('.//span/text()')[0].extract()
                item['percentChange'] = sel.xpath('.//td')[3].xpath('.//span/text()')[0].extract()
                yield item
