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

#声明一个全局的变量，存放所有可执行的爬虫
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
				print "\t\t--show\t\t显示当前可运行的spider"
				print "\t\t--spider +name\t\t运行指定spider"
				print "\t\t--spider_name\t\tkill指定spider"
				print "\t\t--version\t\t版本查询"
				print "\t\t--alive\t\t\t查询所有存活spider"
				print "\t\t--run_all\t\t运行全部spider"
				print "\t\t--killall\t\t杀死所有spider"
		elif option == "run_all":
				spider_name = spider_name
				for spider in spider_name:
						if not re.search('2',spider):
								#用当天的日期来做日志文件名
								command = "nohup scrapy crawl %s >> mv_spider.%s.log 2>&1 &"%(spider,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
								os.system(command)
								print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
		elif option == "show":
				print "config文件中所有的spider有 ，共%s个:\n %s\t\t\t\n"%(len(spider_name),(' , '.join(spider_name)))
				running = []
				for spider in spider_name:
						exists = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider)
						running.append(spider) if exists else ""
				print "其中处于running状态的有 ，共%s个:\n %s \t\t\t\n"%(len(running),(' , '.join(running)))
				stop = list(set(spider_name)^set(running))
				print "其中处于stop状态的有 ，共%s个:\n %s \t\t\t\n"%(len(stop),(' , '.join(stop)))
				
		elif option == "spider":
				try:
						spider = sys.argv[2]
				except Exception,e:
						print "请不要输入空的spider name , 退出."
						sys.exit()
				if spider in spider_name:
						command = "nohup scrapy crawl %s >> mv_spider.%s.log 2>&1 &"%(spider,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
						os.system(command)
						print "正在寻找spider %s 是否启动，稍等......"%spider
						time.sleep(1)
						print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
				else:
						print "请输入正确的spider name."		
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






