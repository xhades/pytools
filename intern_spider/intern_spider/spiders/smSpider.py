#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__  = 'xhades'

import scrapy
import platform
from selenium import webdriver
from scrapy.spiders import CrawlSpider
from intern_spider.items import InternSpiderItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from intern_spider.platform_diy import getPlatform


name = 'sm'
base_url = 'http://www.newsmth.net/nForum/#!board/Intern'
start_urls = [base_url]
start_urls.extend([base_url+'?p='+str(i) for i in range(2,4)])
# print start_urls
getPlatform = platform.system()


def __init__(self):
    scrapy.spiders.Spider.__init__(self)
    if self.platform == 'linux':
        self.driver = webdriver.PhantomJs()
    elif self.platform == 'win':
        pass
    self.driver.set_page_load_timeout(10)
    dispatcher.connect




