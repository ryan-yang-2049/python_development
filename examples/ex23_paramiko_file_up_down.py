#!/usr/bin/env python3
#coding:utf-8
'''
实现文件的上传下载，put上传，get下载
'''
import paramiko

transport = paramiko.Transport(('106.15.200.102',22))
transport.connect(username='oracle',password='oracle')

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('/scripts/python_development/note.md','/tmp/test.md')
sftp.get('/tmp/aa.txt','/tmp/aa.txt')
transport.close()
