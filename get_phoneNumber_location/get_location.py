# !/usr/bin/env python
# -*- coding:utf-8 -*-
num_list = ['num1','num2','num3']
import  urllib2, json

location_dict = {}

# 获取归属地


def get_phone_location(phone):
    url = 'http://apis.baidu.com/apistore/mobilenumber/mobilenumber?phone=%s'%(phone)
    req = urllib2.Request(url)
    req.add_header("apikey", "986006f8e42fc87cad593060df2bc347")
    resp = urllib2.urlopen(req)
    content = json.loads(resp.read())
    # print content
    location = content['retData']['city']
    if location_dict.has_key(location):
        location_dict[location] +=1
    else:
        location_dict[location] =1

#  读取所有号码
for phone in num_list:
    get_phone_location(phone)

print location_dict
