'''
Created on 2013-2-4

@author: Administrator
'''
import win32console
import time

lp=win32console.GetConsoleProcessList()
s=''
for p in lp:
    s+='%d ' %(p)
win32console.SetConsoleTitle(s)
print(s)
print ('hello world')
for x in range(1,100):
    print (s)

time.sleep(10)
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
#        newbuf.WriteConsole(s)
        print (s)
    #time.sleep(10)
    
    
time.sleep(100)