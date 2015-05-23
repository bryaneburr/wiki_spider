# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3 as sql
import scrapy.exceptions.DropItem

class WikiCompanysizePipeline(object):
	# create our db if it doesn't exist already:
	def __init__(self):
		self.dbcon = sql.connect('results.db')
		with self.dbcon:
			cur = self.dbcon.cursor()
			cur.execute('CREATE TABLE IF NOT EXISTS companies(id INTEGER PRIMARY KEY, name STRING, employees INTEGER, as_of INTEGER);')

    def process_item(self, item, spider):
    	if hasattr(item, 'employees'):
    		with self.dbcon:
    			cur = self.dbcon.cursor()
    			insert = (item['name'], item['employees'], item['as_of'])
    			# passing a value of NULL to an integer primary key will cause the integer to autoincrement (sqlite3 quirk),
    			# which is what we want here:
    			cur.execute('INSERT INTO companies VALUES (NULL, ?, ?, ?)', insert)
    		return item
    	else:
    		raise DropItem('Item missing necessary info, dropping item...')
