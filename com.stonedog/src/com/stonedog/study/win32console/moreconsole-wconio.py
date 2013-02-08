#encoding=utf-8
'''
Created on 2013-2-4

@author: Administrator
'''
import win32console,time,sys
import WConio
win32console.AllocConsole()
 

sys.stdout=open('CONOUT$','w',0)

newbuf=win32console.CreateConsoleScreenBuffer()
screeninfo=newbuf.GetConsoleScreenBufferInfo()

#print screeninfo

newbuf.SetConsoleActiveScreenBuffer()



#Display something in low video
WConio.lowvideo()
newbuf.WriteConsole("Low video\r\n")

#Display something in high video
WConio.highvideo()
newbuf.WriteConsole("High video\r\n")

#Display something in normal video
WConio.normvideo()
newbuf.WriteConsole("Normal video\r\n")

old_setting = WConio.gettextinfo()[4] & 0x00FF #保存默认文本颜色
WConio.textcolor(WConio.RED) #将后续输出的文本的颜色设为红色
#WConio.cputs("\n\nPress any key to end\r\n")
newbuf.WriteConsole('hello world\r\n')

WConio.textattr(old_setting)
newbuf.WriteConsole('hello world\r\n')


time.sleep(100)