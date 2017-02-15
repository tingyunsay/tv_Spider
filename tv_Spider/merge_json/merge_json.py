#!/usr/bin/env python
# -*- coding:utf-8 -*-  
import sys,os
import json
import commands
import re


all_json_name = map(lambda x:x.replace('.',''),re.findall('.+\.',commands.getoutput('ls *.json')))

with open('all_mv.json','w') as f:
		for name in all_json_name:
					a = open("%s.json"%name,'r')
					f.write(a.read())




