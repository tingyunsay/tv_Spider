# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import twisted
from scrapy import log
from scrapy.exceptions import DropItem
from pybloomfilter import BloomFilter
from scrapy.exceptions import CloseSpider
import re
import time
import os
from twisted.enterprise import adbapi
import MySQLdb.cursors

#itemloader输出得到的list提取成str
def list_2_str(temp):
	return ' '.join(temp)




class tvSpiderPipeline(object):
	def __init__(self):
		self.file = codecs.open('tempfile.json','wb',encoding="utf-8")
	def process_item(self, item, spider):
		line = json.dumps(dict(item),ensure_ascii=False)+"\n"
		self.file.write(line)



class SQLPipeline(object):
	def __init__(self):
		self.dbpool=adbapi.ConnectionPool('MySQLdb',
				host='127.0.0.1',
				db='liaohong_test',
				user='root',
				passwd='liaohong',
				cursorclass=MySQLdb.cursors.DictCursor,
				charset='utf8',
				use_unicode=True)
	def process_item(self,item,spider):
		query=self.dbpool.runInteraction(self.conditional_insert,item)
		query.addErrback(self.handle_error)
		return item
	def conditional_insert(self,tx,item):
		tx.execute("insert into artist_concert2(performer,concert_place,concert_time,concert_title,concert_price) values(%s,%s,%s,%s,%s)",(item['performer'],item['concert_place'],list_2_str(item['concert_time']),item['concert_title'],list_2_str(item['concert_price'])))
	def handle_error(self,e):
		log.err(e)
	
	
	
