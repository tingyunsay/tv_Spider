#!coding=utf-8

#这个文件：分离出所有需要计算站点实际page页面的木块，一个可扩展的if elif语句来实现

def Total_page_circulate(site_name,max_pages):
	if site_name == "tudou_show":
			return (max_pages/90)+1
	elif site_name == "letv_show":
			return (max_pages/30)+1
	elif site_name == "tudou_sp":
			return (max_pages/90)+1
	elif site_name == "letv_sp":
			return (max_pages/30)+1
	else:
			return max_pages


def Turn_True_Page(i,site_name):
	if site_name == "tencent_show":
			return (i - 1)*30
	else:
			return i



def Total_page_circulate2(site_name,max_pages):
	if site_name == "tudou_show":
			return (max_pages/90)+1
	elif site_name == "tudou_sp":
			return (max_pages/90)+1
	else:
			return max_pages







