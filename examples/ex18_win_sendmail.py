#!/usr/bin/env python3
#coding:utf-8
import smtplib
import email.mime.multipart
import email.mime.text

def send_mail(message):
    mailto_list = ["yangyang@phc-dow.com","jenkins@phc-dow.com"]
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'ryan9093@163.com'             #发件人地址
    msg['to'] = ";".join(mailto_list)           #收件人地址
    msg['subject'] = 'python3 smtp test'         #主题
    content = '''''
        你好，这是一封自动发送的邮件。

        内容为：%s

    ''' % (message)    #发件内容
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')                    #发件箱服务器以及端口
    smtp.login('ryan9093@163.com', 'ryan461580544')     #发件箱，以及发件箱的smtp认证码
    smtp.sendmail('ryan9093@163.com', mailto_list, str(msg))   #发件箱，收件箱，
    smtp.quit()

mess = "python3 邮件测试"
send_mail(mess)