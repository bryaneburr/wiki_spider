from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from wiki_companysize.items import WikiCompanysizeItem

class WikiSpiderSpider(CrawlSpider):
    name = 'wiki_spider'
    # restrict our search to english wikipedia
    allowed_domains = ['en.wikipedia.org']
    start_urls = [#'http://www.en.wikipedia.org/'
                  'http://en.wikipedia.org/wiki/Apple_Inc.',
                  'http://en.wikipedia.org/wiki/Oracle_Corporation',
                  'http://en.wikipedia.org/wiki/Microsoft',
                  'http://en.wikipedia.org/wiki/Lists_of_companies'
                 ]
    # follow all links on page that point to any valid wikipedia page
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=['//*[@id="mw-content-text"]']), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        i = WikiCompanysizeItem()
        # grab info-box table(s)
        tables = sel.xpath('//*[@class="infobox vcard"]')
        for table in tables:
            # check <tr>'s for string "Number of employees" in a <th><div>:
            for tr in table.xpath('.//tr'):
                if tr.xpath('.//th/div/text()').extract() == [u'Number of employees']:
                    # extract data we want 
                    i['employees'] = tr.xpath('.//td/text()').extract()[0]
                    i['name'] = sel.xpath('//*[@id="firstHeading"]/text()').extract()[0]
                    print "Company: %s, number of employees: %s" % (i['name'], i['employees'])
                    # if we've found what we're after, we're done, return the item:
                    return i
       # won't get here unless nothing is found on the page matching what we want - 
       # empty items are handled by the pipeline, so we don't check here:
        return i
