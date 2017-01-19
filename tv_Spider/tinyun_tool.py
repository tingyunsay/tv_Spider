#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import re
import time
import subprocess
import commands

def is_runing(spider_name):
	a = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider_name)
	return True if a else False	
def get_pid(exists):
	return re.search("\d+",exists).group() if exists else None
def kill_pid(pid):
	return True if not (os.system("kill -9 %s"%pid) if pid else 1) else False
	
	#return True if not os.system("kill -9 %s"%pid) else False

spider_name = []

with open('config.json','r') as f:
		spider_name = eval(f.read()).keys()

#删除全部spider
if len(sys.argv) < 2:
		print "参数过少，请根据 --help操作!"

elif sys.argv[1].startswith('--'):
		option = sys.argv[1][2:]
		if option == "help":
				print "输入如下格式:"
				print "\t\t--spider_name\t\tkill指定spider"
				print "\t\t--version\t\t版本查询"
				print "\t\t--alive\t\t\t查询所有存活spider"
				print "\t\t--killall\t\t杀死所有spider"
		elif option == "version":
				print "version 1.0 tingyun"
		elif option == "alive":
				res = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						res.append(spider) if exists else ""
				print "the total of live spider are %s , and every signal is :\n\t%s"%(len(res),(','.join(res))) if res else "no spider is alive..."				
		elif option == "killall":
				res = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						if kill_pid(get_pid(exists)):
								res.append(spider)
				print "all killed %s spiders , and every signal is :\n\t\t%s"%(len(res),','.join(res)) if len(res) > 0 else "no spider is killed"
		else:
				exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%option)
				if kill_pid(get_pid(exists)):
						print "kill spider %s success...."%option
				else:
						print "spider %s not found !!!"%option
else:
		print "未知参数，退出...."






