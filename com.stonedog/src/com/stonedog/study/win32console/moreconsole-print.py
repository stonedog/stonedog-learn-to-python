'''
Created on 2013-2-4

@author: Administrator
'''
import win32console,time,sys
win32console.AllocConsole()


lp=win32console.GetConsoleProcessList()
s=''
for p in lp:
    s+='see the screen %d ' %(p)
win32console.SetConsoleTitle(s)
sys.stdout=open('CONOUT$','w',0)
print(s)
time.sleep(10)


