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

# Set number of concurrent requests (16 is probably a good place to start, 
# increase this quantity if you have more cores available)
CONCURRENT_REQUESTS = 16

# Depth limit for crawler (kind of necessary for this project, considering we 
# probably don't want to crawl all 9.7 Gb of english wikipedia) - I've found
# that a depth limit of 10 grabs a good amount of data (takes a while, though)
DEPTH_LIMIT = 10

# These options guarantee breadth-first search, which is better for our purposes
# see http://doc.scrapy.org/en/latest/faq.html#does-scrapy-crawl-in-breadth-first-or-depth-first-order
# for more info
# (comment out the following three lines to revert to depth-first search)
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

