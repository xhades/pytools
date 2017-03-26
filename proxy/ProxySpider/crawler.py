#! /usr/env/bin python
# -*-coding:utf-8-*-
import re
import time
import requests
from lxml import etree
import logging


# get PROXY
class ProxyGet(object):
    def __init__(self):
        self.START_REQ_URL = 'http://www.xicidaili.com/nn/1'  # xici

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            'If-None-Match': 'W/"55137f1b0b95274c73426d578bd9d2d7"',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.95 Safari/537.36'
        }
        self.TOTAL_PAGE = self.get_total_page()

    def get_total_page(self):
        rsponse = requests.get(self.START_REQ_URL, headers=self.headers)
        # get total page
        html_body = etree.HTML(rsponse.text)
        total_page = html_body.xpath("//div[@class='pagination']/a[last()-1]//text()")[0]
        return total_page

    def get_ip(self, url=None):
        IPResult = []
        page_rsponse = requests.get(url=url, headers=self.headers)
        selector = etree.HTML(page_rsponse.text)
        tr_result = selector.xpath("//table[@id='ip_list']//tr")
        tr_no = len(tr_result)
        for i in xrange(2, int(tr_no)+1):
            ip = selector.xpath("//table[@id='ip_list']//tr[{}]/td[2]//text()".format(i))[0]
            port = selector.xpath("//table[@id='ip_list']//tr[{}]/td[3]//text()".format(i))[0]
            proxies = {
                "http": "http://{}:{}".format(ip, port),
            }
            resp = requests.get(url='https://www.baidu.com/', proxies=proxies, timeout=240)
            if resp.status_code==200:
                IPResult.append((ip, port))
                print proxies
        return IPResult


if __name__ == '__main__':
    # instance
    proxy = ProxyGet()
    ip_result = proxy.get_ip(url='http://www.xicidaili.com/nn/2')
    print ip_result
