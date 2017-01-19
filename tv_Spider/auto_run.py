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


def is_runing(spider_name):
        a = commands.getoutput("ps -ef|grep %s|grep -v grep"%spider_name)
        return True if a else False

#声明一个全局的变量，存放所有可执行的爬虫
res = []
if len(sys.argv) < 2:
        print "参数过少, 请输入 --help 查看命令."
elif sys.argv[1].startswith('--'):
        with open('config.json','r') as f:
                spider_name = eval(f.read()).keys()
                for spider in spider_name[:]:
                        if not re.search('2',spider):
                                res.append(spider)
		
		option = sys.argv[1][2:]
		if option == "help":
				print "输入如下格式:"
				print "\t\t--run_all\t\t运行全部spider"
				print "\t\t--spider +name\t\t运行指定spider"
				print "\t\t--show\t\t显示当前可运行的spider"
		elif option == "run_all":
				spider_name = res
				for spider in spider_name:
						if not re.search('2',spider):
								#用当天的日期来做日志文件名
								command = "nohup scrapy crawl %s >> mv_spider.%s.log 2>&1 &"%(spider,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
								os.system(command)
								print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
		elif option == "show":
				print "你可以抓取的spider有 ，共%s个:\n %s\t\t\t\n"%(len(res),(' , '.join(res)))	
		elif option == "spider":
				try:
						spider = sys.argv[2]
				except Exception,e:
						print "请不要输入空的spider name , 退出."
						sys.exit()
				if spider in res:
						command = "nohup scrapy crawl %s >> mv_spider.%s.log 2>&1 &"%(spider,(time.strftime("%Y-%m-%d",time.localtime())).replace(' ','-'))
						os.system(command)
						print "正在寻找spider %s 是否启动，稍等......"%spider
						time.sleep(1)
						print "spider %s is runing ...."%spider if is_runing(spider) else "spider %s start fail ...."%spider
				else:
						print "请输入正确的spider name."
		else:
				print "未知参数，请输入 --help 查看命令."
else:
		print "参数不是以--开头，请重新输入."





"""
with open('config.json','r') as f:
		spider_name = eval(f.read()).keys()
		for spider in spider_name[2:3]:
				command = "nohup scrapy crawl %s >> mv_spider.%s.log 2>&1 &"%(spider,(time.strftime("%Y-%m-%d %X",time.localtime())).replace(' ','-'))
				os.system(command)
				if is_runing(spider):
						print "spider %s is runing ...."%spider
				else:
						print "spider %s start fail ...."%spider

"""
