#!coding=utf-8

#这个文件：分离出所有需要计算站点实际page页面的模块，一个可扩展的if elif语句来实现

#这个是对所有的第一级页面的总的page数的一个统计
def Total_page_circulate(site_name,max_pages):
	if site_name == "tudou_tv":
			return (max_pages/90)+1
	else:
			return max_pages


def Turn_True_Page(i,site_name):
	if site_name == "douban_tv":
			return (i - 1)*20
	else:
			return i


#这个在除了第一级页面，之后可能会分多页面的次级的页面（例如虾米专辑：第一级分了很多艺人名字的页面，然后进入到某个艺人的专辑页面，由于专辑数比较多，又分成了多个同级页面）
def Total_page_circulate2(site_name,max_pages):
	if site_name == "tudou_show":
			return (max_pages/90)+1
	elif site_name == "tudou_sp":
			return (max_pages/90)+1
	else:
			return max_pages







