# Scrapy settings for wiki_companysize project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'wiki_companysize'

SPIDER_MODULES = ['wiki_companysize.spiders']
NEWSPIDER_MODULE = 'wiki_companysize.spiders'

# Crawl responsibly by identifying yourself
USER_AGENT = 'Scrapy/0.22.2'

# Respect robots.txt
ROBOTSTXT_OBEY = True

# Define our item pipeline(s)
ITEM_PIPELINES = {'wiki_companysize.pipelines.WikiCompanysizePipeline': 100}
