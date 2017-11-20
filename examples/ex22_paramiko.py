#!/usr/bin/env python3
#coding:utf-8
'''
ssh 远程连接，并执行命令返回结果
'''
import paramiko
import os,sys

host = '106.15.200.102'
user = 'oracle'
password = 'oracle'

s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(host,22,user,password,timeout=5)
while True:
	cmd = input('请输入cmd：')
	stdin,stdout,stderr = s.exec_command(cmd)
	cmd_result = stdout.read(),stderr.read()
	for line in cmd_result:
		print(line,)
s.close()
