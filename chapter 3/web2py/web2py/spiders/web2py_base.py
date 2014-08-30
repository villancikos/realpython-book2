from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from web2py.items import Web2PyItem
from bs4 import BeautifulSoup
from urllib2 import urlopen

class MySpider(BaseSpider):
    name = 'web2py'
    allowed_domains = ["web2py.com"]
    start_urls = ["http://www.web2py.com/"]
    htmlPage = urlopen(start_urls[0]).read()
    mySoup = BeautifulSoup(htmlPage)


    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//a')
        items = []
        for title in items:
            item = Web2PyItem()
            item["title"] = title.select("/text()").extract()
            item["url"] = title.select("/@href").extract()
            items.append(item)
        return(items)
