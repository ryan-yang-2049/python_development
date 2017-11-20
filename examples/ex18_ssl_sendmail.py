#!/usr/bin/env python3
#coding:utf-8
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def send_email(from_addr,to_addr,message,password):
	context = '''
		python ssl 邮件测试。
		
		内容为：%s
	
	''' % (message)
	msg = MIMEText(context,'html','utf-8')
	msg['From'] = '<%s>' % from_addr
	msg['To'] = '<%s>' % to_addr
	msg['Subject'] = "python SSL邮件测试"
	
	smtp = smtplib.SMTP_SSL('smtp.163.com',465)
	smtp.set_debuglevel(1)
	smtp.ehlo("smtp.163.com")
	smtp.login(from_addr,password)
	smtp.sendmail(from_addr, [to_addr], msg.as_string)
	
	
if __name__ == '__main__':
	mess = "这是一个晴朗的早晨"
	send_email("ryan9093@163.com","809074558@qq.com",mess,"ryan461580544")
