#-*- coding:utf-8 -*-

import scrapy
from mySpider.items import ItcastItem

#创建一个爬虫类
class ItcastSpider(scrapy.Spider):
	# 爬虫名，执行的时候安装爬虫名来
	name = "itcast"
	# 允许爬虫作用的范围
	allowd_domains = ["http://www.itcast.cn/"]
	# 爬虫起始的url
	start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

	def parse(self,response):
#		with open("teacher.html","w") as f:
#			f.write(response.body)
		teacher_list = response.xpath('//div[@class="li_txt"]');
		# 所有老师信息的集合
		teacherItem = []
		for each in teacher_list:
			# 实例化一个对象
			item = ItcastItem()
			name = each.xpath('./h3/text()').extract()
			title =  each.xpath('./h4/text()').extract()
			info = each.xpath('./p/text()').extract()
		
			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] =info[0]
			teacherItem.append(item)
#			print(name[0])
#			print(title[0])
#			print(info[0])
			yield item
		#return teacherItem
