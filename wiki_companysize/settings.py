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

# Don't need to accept cookies
COOKIES_ENABLED = False

# Don't need to follow redirects since we'll be working with wikipedia urls
REDIRECT_ENABLED = False

# Set logging level (should be INFO for production code, DEBUG for development)
LOG_LEVEL = 'INFO'

# Set number of concurrent requests
CONCURRENT_REQUESTS = 100

