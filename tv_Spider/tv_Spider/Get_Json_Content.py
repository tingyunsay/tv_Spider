#!coding=utf-8

import json
import requests

def Get_Json_Content(urls , spider_name):
		if spider_name == "letv_tv":
				target_url = "http://v.stat.letv.com/vplay/queryMmsTotalPCount?pid={pid}"
				return requests.get(target_url.format(pid=urls)).json()
		else:
				return urls

