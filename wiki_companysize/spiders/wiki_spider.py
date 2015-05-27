from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wiki_companysize.items import WikiCompanysizeItem

class WikiSpiderSpider(CrawlSpider):
    name = 'wiki_spider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [#'http://www.en.wikipedia.org/'
                    'en.wikipedia.org/wiki/Apple_Inc.'
                 ]

    # follow all links on page that point to any valid wikipedia page
    rules = (
        Rule(LinkExtractor(allow=r'/*'), callback='parse_item', follow=False, restrict_xpaths=('//*[@id="mw-content-text"]')),
    )

    def parse_item(self, response):
        sel = Selector(response)
        i = WikiCompanysizeItem()
        tables = sel.xpath('//*[@id="mw-content-text"]/table')
        # the data we're looking for is contained within a table (we don't know which table, so we gotta check 'em all):
        for table in tables:
            # check <tr>'s for string "Number of employees" in a <th><div>:
            for tr in table.xpath('.//tr'):
                if tr.xpath('.//th/div/text()').extract() == [u'Number of employees']:
                    # extract data we want 
                    i['employees'] = int(tr.xpath('.//td/text()').extract()[0]replace(',', '').split()[0])
                    i['name'] = sel.xpath('//*[@id="firstHeading"]/text()').extract()[0]
                    # if we've found what we're after, we're done:
                    break
        # turn over item to pipeline for processing:
        return i
