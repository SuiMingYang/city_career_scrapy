# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonCityDataItem(scrapy.Item):
    # define the fields for your item here like:
    cityname = scrapy.Field() #城市名称
    company = scrapy.Field() #公司名称
    experience = scrapy.Field() #需要经验
    education = scrapy.Field() #学历要求
    salary = scrapy.Field() #薪资待遇
    company_size = scrapy.Field() #公司规模
    industry = scrapy.Field() #所属行业
    recruiter = scrapy.Field() #招聘人信息
    #publishdate = scrapy.Field() #发布时间
    
