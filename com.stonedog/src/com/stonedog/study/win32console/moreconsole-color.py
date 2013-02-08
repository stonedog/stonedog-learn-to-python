#encoding=utf-8
'''
Created on 2013-2-2

@author: Administrator
'''
import win32console,time,sys
win32console.AllocConsole()

RED=4
LIGHTRED=12
YELLOW=14
lp=win32console.GetConsoleProcessList()
s=''
for p in lp:
    s+='%d ' %(p)
win32console.SetConsoleTitle(s)
sys.stdout=open('CONOUT$','w',0)
#sys.stdin=open('CONIN$','w',0)
newbuf=win32console.CreateConsoleScreenBuffer()

#newbuf.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
newbuf.SetConsoleActiveScreenBuffer()
#time.sleep(10)
s='%10s : %10d : %10d' %('user',100,10)
#newbuf.SetConsoleTextAttribute(win32console.FOREGROUND_RED|win32console.FOREGROUND_INTENSITY
#        |win32console.BACKGROUND_GREEN|win32console.BACKGROUND_INTENSITY)
for b in range(0,16):
    for f in range(0,16):
        newbuf.SetConsoleTextAttribute((b<<4)|f)
        s='BackGroundColor=%4d :ForeGroundColor=%4d \r\n' %(b,f)
        newbuf.WriteConsole(s)
    time.sleep(10)


