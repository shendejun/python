# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']
    
    url = "https://hr.tencent.com/position.php?&start="    
    offset = 0
    # 第一次爬取的地址
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
		# 初始化模型对象
		item = TencentItem()
		# 职位名 
		# 把xpth结果转成uncode字符串，在取第一个
		item['positionname'] = positionname = each.xpath("./td[1]/a/text()").extract()[0]
		# 详情链接
		item['positionlink'] = positionlink = each.xpath("./td[1]/a/@href").extract()[0]
		# 职位类别
		item['positionType'] = positionType = each.xpath("./td[2]/text()").extract()[0]
		# 招聘人数
		item['peopleNum'] = peopleNum = each.xpath("./td[3]/text()").extract()[0]
		# 工作地点
		item['workLocation'] = workLocation = each.xpath("./td[4]/text()").extract()[0]
		# 发布时间
		item['publishTime'] = publishTime = each.xpath("./td[5]/text()").extract()[0]

		
		# 将数据交给管道文件处理
		yield item


	if self.offset <= 50:
		self.offset += 10
		
	#  每次处理完一页数据之后，重新发送下一页请求
	# 将请求重新发送给调度器入队列，出队列，交给下载器下载
	# 如果地址重复就不会重复请求
	yield scrapy.Request(self.url + str(self.offset),callback = self.parse)


