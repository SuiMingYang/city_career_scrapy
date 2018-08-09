# -*- coding: utf-8 -*-
import scrapy
from python_city_data.items import PythonCityDataItem
from urllib import parse
'''
在boss直聘上，分析各城市的python招聘信息
smy
2018-07-31
'''

base_url="https://www.zhipin.com/job_detail/?query=python&scity=%s&industry=&position="
selected_city=['北京','杭州','武汉','成都','长沙']
selected_codes=['101010100','101210100','101200100','101270100','101250100']
class PythonDataSpiderSpider(scrapy.Spider):
    name = 'python_data_spider'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']
    
    def parse(self, response):
        #city_name=response.xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/div[1]/text()')
        for selected_code in selected_codes:
            # 依次遍历城市URL
            city_detail_url = base_url % selected_code
            # 解析每个城市的月份数据
            request = scrapy.Request(city_detail_url, callback=self.parse_detail)
            yield request

    def parse_detail(self, response):
        city_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        item = PythonCityDataItem()
        for city_detail in city_list:
            # 依次遍历城市URL
            info_primary=city_detail.xpath('.//div/div[1]')
            info_company=city_detail.xpath('.//div/div[2]')
            info_publis=city_detail.xpath('.//div/div[3]')
            # 解析每个城市的月份数据
            item['cityname'] = info_primary.xpath('.//p/text()').extract()[0]
            item['company'] = info_company.xpath('.//div/h3/a/text()').extract_first() 
            item['experience'] =  info_primary.xpath('.//p/text()').extract()[1]
            item['education'] = info_primary.xpath('.//p/text()').extract()[2] #if len(info_primary.xpath('.//p/text()').extract())==3 else ""
            item['salary'] = info_primary.xpath('.//h3/a/span/text()').extract_first() 
            item['company_size'] = info_company.xpath('.//div/p/text()').extract()[2] if len(info_company.xpath('.//div/p/text()').extract())==3 else ""
            item['industry'] = info_company.xpath('.//div/p/text()').extract()[0]
            item['recruiter'] = info_publis.xpath('.//h3/text()').extract_first() 
            #item['publishdate'] = info_publis.xpath('.//p/text()').extract_first() 

            print(item)
            yield item
            