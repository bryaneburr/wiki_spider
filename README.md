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

## FAQ

##### Why did you use sqlite3 to store the data? Why not MySQL/Postgres/Mongo/etc.?

##### Why did you pick these specific starting urls?

##### What's wrong with Depth-First search?

##### Why do you store the company size as a string and not an integer? Wouldn't integers be easier to work with/ make more sense?

##### 
