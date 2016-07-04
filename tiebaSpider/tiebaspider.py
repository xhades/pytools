# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:xhades
# version:1.0

import sys
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import json
import requests

reload(sys)

sys.setdefaultencoding('utf-8')  #设置编码


def towrite(contentdict):
    f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
        author = reply_info['author']['user_name']
        content = each.xpath('div[@class="d_post_content_main"]/div[@class=class="p_content  p_content p_content_icon_row1 p_content_nameplate"]/cc/div[@class="d_post_content j_d_post_content clearfix"]/text()')
        reply_time = reply_info['content']['date']
        print content   # content为空列表 目前还未解决这个问题
        print reply_time
        print author
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time
        towrite(item)


if __name__ == '__main__':
    pool = ThreadPool(4)
    f = open('content.txt','a')
    page = []
    for i in range(1,3):
        newpage = 'http://tieba.baidu.com/p/4609646212?pn=' + str(i)
        page.append(newpage)

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
