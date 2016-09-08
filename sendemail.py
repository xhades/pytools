#!/usr/bin/env python
#-*-coding:utf-8 -*-
__author__ = 'xhades'
#date: 4/9/2016

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host="smtp.yeah.net"  #设置服务器
mail_user="augusteyy@yeah.net"    #用户名
mail_pass="dahaiwei424"   #口令 
mail_postfix = '163.com'
sender = 'augusteyy@yeah.net'
receivers = ['420793534@qq.com']

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('大海威','utf-8')
message['To'] = Header('TZ','utf-8')
subject = 'Python脚本'
message['Subject'] = Header(subject,'utf-8')

# 邮件正文
message.attach(MIMEText('这是发送邮件测试脚本','plain','utf-8'))

# 构造附件 传送当前目录下test.txt文件
att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

try:
    smtpObj = smtplib.SMTP()
    print 'error1'
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    print 'error3'
    smtpObj.login(mail_user,mail_pass) 
    print 'error2' 
    smtpObj.sendmail(sender, receivers, message.as_string())
    print '邮件发送成功'
except smtplib.SMTPException:
    print "Error: 无法发送邮件"