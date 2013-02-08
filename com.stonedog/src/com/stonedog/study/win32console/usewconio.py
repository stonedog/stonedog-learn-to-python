'''
Created on 2013-2-4

@author: Administrator
'''

import time
import  win32console 
import win32file
import win32api


def GetConsoleOut():
    #return CreateFile('CONOUT$',win32file.GENERIC_READ|win32file.GENERIC_WRITE,win32file.FILE_SHARE_READ|win32file.FILE_SHARE_WRITE,None,win32file.OPEN_EXISTING,0,0)
    return win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)

def GetOldSetting():
    hd=GetConsoleOut()
    attrs=hd.GetConsoleScreenBufferInfo()
    print attrs
    oldset=attrs['Attributes'] & 0x00FF 
    win32api.CloseHandle(hd)
    return oldset

def TextAttr(color):
    hd=GetConsoleOut()
    attrs=hd.GetConsoleScreenBufferInfo()
    hd.SetConsoleTextAttribute(color)
    win32api.CloseHandle(hd)
    
    
#WConio.highvideo()


#old_setting = WConio.gettextinfo()[4] & 0x00FF

oldset=GetOldSetting()

print ('old seting=%d' % oldset)
time.sleep(2)
for b in range(0,16):
    for f in range(0,16):
        TextAttr((b<<4)|f)
        s='BackGroundColor=%4d :ForeGroundColor=%4d \r\n' %(b,f)
        print(s)
    TextAttr(oldset)
    print('hello world')
    time.sleep(1)

TextAttr(oldset)
print ('hello world we are back')
    
time.sleep(100)        