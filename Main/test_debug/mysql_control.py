#coding=utf-8

import platform
import os

sysstr = platform.system()

if(sysstr =="Windows"):
    ret_msg = os.popen('net start mysql')
    print(ret_msg.read())
elif(sysstr == "Linux"):
    print ("print server mysqld start")
else:
    print ("Other System tasks")