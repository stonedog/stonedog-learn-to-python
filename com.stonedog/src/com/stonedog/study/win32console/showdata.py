#encoding=utf-8
'''
Created on 2013-2-2

@author: Administrator
'''
import win32console
import sys,time
try:
    win32console.AllocConsole()
#    newbuff=win32console.CreateControlScreenBuffer()
#    newbuff.SetStdHandle(win32console.STD_OUTPUT_HANDLE)
except Exception,errdata:
    pass
sys.stdout=open('CONOUT$','w',0)

l_flag=True
#print(u'这是新窗口')
while l_flag:
    s=sys.stdin.readline()
    if not s:
        time.sleep(2)
    elif s=='XX\n':
        l_flag=False
    else:       
      sys.stdout.write(s)
      sys.stdout.flush()
    

      
