# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xhades
# date:6/23/2016
# version:1.0

import MySQLdb as mdb #导入mysql
import xlrd,xlwt  #导入xlrd,xlwt处理excel
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

'''
连接数据库
'''
try:
	conn = mdb.connect (host = "localhost", user = "user", passwd = "", db = "db_name",charset='utf8')  # charset = utf8 不然会中文乱码
except:
	print('open database error')

cursor = conn.cursor ()

'''
er_search_log
'''
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet1')

search_list = []
cursor.execute("SELECT * FROM er_search_log WHERE create_time >'2016-06-09 0:00:00'order by create_time asc")

search_list = cursor.fetchall()
rowlen = len(search_list)
for i in xrange(rowlen):
	for j in xrange(24):
		sheet.write(i,j,search_list[i][j])

wbk.save('F:/work/data0622/search_log.xls')
print '已经成功保存excel文件'

'''
2.总注册记录
user_id
'''
'''
reg_list = []
wbk1 = xlwt.Workbook()
sheet1 = wbk1.add_sheet('sheet1')
cursor.execute("SELECT user_id,user_tel,queries,MID(a.reg_time,1,10) AS reg_date,a.status,type FROM er_user AS a WHERE reg_time>='2016-06-09 0:00:00'")
reg_list = cursor.fetchall()
for i in xrange(len(reg_list)):
	for j in xrange(10):
		sheet1.write(i,j,reg_list[i][j])

wbk1.save('F:/work/data0622/reg_all.xls')

'''

'''
有查询记录用户数
'''
cursor.execute("SELECT COUNT(DISTINCT a.user_id)from (SELECT user_id ,create_time FROM er_search_log WHERE create_time BETWEEN '2016-06-09 0:00:00' AND '2016-06-18 23:59:59' ) AS a LEFT JOIN (SELECT user_id ,create_time FROM er_search_log WHERE create_time BETWEEN '2016-06-20 0:00:00' AND '2016-06-23 23:59:59' ) AS b ON a.user_id=b.user_id ")

check_number = cursor.fetchall()

print '6.9-6.18查询用户数：', check_number
