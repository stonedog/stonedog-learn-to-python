'''
Created on 2013-2-4

@author: Administrator
'''
import win32console,time,sys
win32console.AllocConsole()


lp=win32console.GetConsoleProcessList()
s=''
for p in lp:
    s+='%d ' %(p)
win32console.SetConsoleTitle(s)
time.sleep(10)