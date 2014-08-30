# spider.py

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from hackernews.items import HackernewsItem

class MySpider(BaseSpider):
    # Naming the spider
    name = "wiki"

    # allowed domains to scrape
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Category:2014_films"]

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        titles = response.xpath('//tr[@style="vertical-align: top;"]//li')
        items = []
        for title in titles:
            item = WikipediaItem()
            item["title"] = title.select("a/text()").extract()
            item["url"] = title.select("a/@href").extract()
            items.append(item)
        return items


