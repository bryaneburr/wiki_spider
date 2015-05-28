# wiki_spider
Web crawling project for Nitr.io, built using [scrapy](http://scrapy.org/). Scrapes the number of employees from the wikipedia pages of various companies.

## Setup

This web scraper requires the latest version of scrapy. If you don't already have scrapy installed, you can install it with [pip](https://pypi.python.org/pypi/pip):

```
pip install scrapy
```

Or, you can follow the instructions found [here](http://doc.scrapy.org/en/latest/intro/install.html), which may be useful if you're running Windows.

You will also need the `service_identity` module, which can be installed with:

```
pip install service_identity
```

If you already have scrapy installed, be sure you've upgraded to the latest version:

```
pip install --upgrade scrapy
```

Scrapy requires Python 2.7.

## Usage

To scrape wikipedia using the spider, `cd` into the folder that contains `scrapy.cfg` and enter the following command:

```
scrapy crawl wiki_spider
```

To stop the spider while scraping, press `ctrl+C` in the terminal to send `SIGINT` to the process. It may take a few moments to exit gracefully, so please be patient.

## How it works

This scrapy web crawler consists of two main components:

1. A [spider](http://doc.scrapy.org/en/latest/topics/spiders.html) that parses http responses and extracts the desired information (see `wiki_companyzie/spiders/wiki_spider.py`), and
2. A [pipeline](http://doc.scrapy.org/en/latest/topics/item-pipeline.html) that takes items parsed from the response and saves them to an sqlite3 database (see `wiki_companysize/pipelines.py`).

More information about the specifics of the scrapy architecture can be found [here](http://doc.scrapy.org/en/latest/topics/architecture.html).

The `parse_item` method in `wiki_spider.py` searches the html document for an xpath that matches the CSS class of the information sidebar (which is represented using a `<table>`) on a company's wikipedia page. If found, it then searches this table for a `<th>` which contains the text `'Number of employees'`, extracts the text in the corresponding `<td>`, and passes this information, in the form of an `item` (see `wiki_companysize/items.py`) to the pipeline. 

The pipeline ensures that the `item` is not empty, then stores the item's contents in the database. At this time, database records consist of an autoincrementing integer `id`, the `name` of the company, and the corresponding number of `employees`. The number of employees and the company name are both stored as strings (more on this later). 

The crawler will continue until it has reached its maximum depth limit, as defined in `settings.py`.

## Settings

Although scrapy has a variety of [settings](http://doc.scrapy.org/en/latest/topics/settings.html), there are only a few that significantly affect the behavior of this project:

* `CONCURRENT_REQUESTS` sets the number of simultaneous requests that can be made at a given time. I chose a value of 16, as it works well with my system configuration (8 GB RAM, 2 cores), but if you have more cores and/or memory, feel free to increase this setting as you see fit.
* `DEPTH_LIMIT` sets the number of levels the scraper will crawl from the given start url(s). For instance, if I specified a start url of `http://en.wikipedia.org/wiki/Apple_Inc.`, and a `DEPTH_LIMIT` of 1, then the scraper would follow each url on that page, and then stop. Larger values for this setting will cause an exponential increase in the number of pages scraped from wikipedia; use values larger than 10 at your own risk.
* `DEPTH_PRIORITY`, `SCHEDULER_DISK_QUEUE`, and `SCHEDULER_MEMORY_QUEUE` can be used in conjunction to provide breadth-first search (the default is depth-first). Comment out these lines if you'd rather the spider use depth-first search.

## FAQ

##### Why did you use sqlite3 to store the data? Why not MySQL/Postgres/Mongo/etc.?

I chose sqlite3 for a number of reasons:

1. It comes standard on nearly every modern OS.
2. The sqlite3 python library comes standard with python 2.7 and is very easy and straightforward to use.
3. I didn't want to spend a lot of time setting up and administrating another database - it's ready to go right out of the gate.
4. I wanted the database to be portable (IE, you don't have to set up a whole new database on your own machine in order to use the scraper)
 
If I were to deploy this project in more serious settings, I would probably use Postgres, and set up a simple REST service to access the data post-scrape.

##### Why did you pick these specific starting urls?

Web scraping is more of an art than a science. I chose the urls listed in `wiki_spider.py` simply because I felt they would provide a good idea of the functionality of the scraper and provide a large amount of links to crawl. Apple, Oracle, and Microsoft also have relationships with many other companies (which is reflected by their wikipedia pages), so they seemed like a natural starting point. Feel free to try your own strategies.

##### What's wrong with Depth-First search?

Nothing in particular. I found that BFS tends to return more results quicker with this set of starting urls, but it isn't necessary for full functionality.

##### Why do you store the company size as a string and not an integer? Wouldn't integers be easier to work with/ make more sense?

To see why I store company size information as a string and not an integer, take a look at the following sample output from the scraper:

```
...
Company: Société Générale, number of employees: 171,955 
Company: M&G Investments, number of employees: approx 1000 (2008)
Company: PIMCO, number of employees: 2444
Company: Mercury Asset Management, number of employees: 1,300
Company: Panmure Gordon & Co., number of employees: approximately 100
Company: B&R, number of employees: 2,300 worldwide (as of Oct. 2011)
Company: Beckhoff, number of employees: 2800 (
Company: Cognex Corporation, number of employees: 1,017
Company: National Instruments, number of employees: 6,869 
Company: Emerson Electric, number of employees: 115,100 
Company: FANUC, number of employees: 5,261 (consolidated) (as of December 2013)
Company: Omron, number of employees: 35,411 (2013)
Company: Phoenix Contact, number of employees: 12,900
Company: Indramat, number of employees: 1,500 (2001)
Company: Rockwell Automation, number of employees: About 22,500 (2014)
Company: Yaskawa Electric Corporation, number of employees: 10,383 (consolidated)
...
```

As you can see, there *is* some structure and consitency across different pages, but not very much. It seems that there's a lot of variety in the way each company's employment figures are expressed (and often they are not well-formed). As such, I decided that grabbing as much information as possible was the right way to go in this case: further processing is needed to extract the integer value from the text, but it's not at all clear as to the "correct" way to go about this. For instance, how do you express `approx 1000` as an integer? And how should I deal with the fact that some companies' employment figures include a year, and some not? After all, this could be valuable information. 

In the end, I decided upon fault-tolerability and human-readability over simple correctness and structuring of the data - after all, once we have the data, we can post-process it in any way we want, which is probably outside the scope of this project.

***

*Happy scraping!*





