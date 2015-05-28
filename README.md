# wiki_spider
Web crawling project for Nitr.io, built using [scrapy](http://scrapy.org/).

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

To scrape wikipedia using the spider, `cd` into the `wiki_companysize` folder and enter the following command:

```
scrapy crawl wiki_spider
```

To stop the spider while scraping, press `ctrl+C` in the terminal to send `SIGINT` to the process. It may take a few moments to exit gracefully, so please be patient.

#### How it works

#### Settings

## FAQ

##### Why did you use sqlite3 to store the data? Why not MySQL/Postgres/Mongo/etc.?

##### Why did you pick these specific starting urls?

##### What's wrong with Depth-First search?

##### Why do you store the company size as a string and not an integer? Wouldn't integers be easier to work with/ make more sense?

##### 
