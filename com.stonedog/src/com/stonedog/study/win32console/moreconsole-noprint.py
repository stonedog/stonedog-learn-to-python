'''
Created on 2013-2-4

@author: Administrator
'''
import win32console,time,sys
win32console.AllocConsole()


lp=win32console.GetConsoleProcessList()
s=''
wd=win32console.GetConsoleWindow()
for p in lp:
    s+='see the screen %d ' %(p)
s+='window:%d' % wd
win32console.SetConsoleTitle(s)
print(s)
time.sleep(10)