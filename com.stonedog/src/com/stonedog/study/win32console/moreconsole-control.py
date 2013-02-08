#encoding=utf-8
'''
Created on 2013-2-2

@author: Administrator
'''
import subprocess,time
l_flag=True
while l_flag:
    print('Enter Please c:Create  x:Exit')
    ch=raw_input()
    if ch=='x':
        l_flag=False
    elif ch=='c':
        #subprocess.Popen('pythonw moreconsole.py')
        subprocess.check_call('pythonw moreconsole-noprint.py')
    time.sleep(2)
