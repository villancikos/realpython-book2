# wiki.py - basespider

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from wikipedia.items import WikipediaItem
from urlparse import urljoin

class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Category:2014_films"]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//tr[@style="vertical-align: top;"]//li')
        items = []
        for title in titles:
            wiki_item = WikipediaItem()
            url = title.select("a/@href").extract()
            wiki_item["title"] = title.select("a/text()").extract()
            wiki_item["url"] = urljoin("http://en.wikipedia.org",url[0])
            items.append(wiki_item)
        return(items)
