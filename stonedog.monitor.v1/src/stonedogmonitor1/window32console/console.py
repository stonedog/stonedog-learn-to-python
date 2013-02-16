#encoding=utf-8
'''
Created on 2013-2-16

@author: Administrator
'''

 
import win32console
import time
 
 
def WriteLog(s):
    BG_COLOR=0
    FG_COLOR=15
    WriteColorText(s,FG_COLOR,BG_COLOR,swap=False)

def WriteWaring(s):
    W_BG_COLOR=10
    W_FG_COLOR=12
    WriteColorText(s,W_FG_COLOR,W_BG_COLOR,swap=False)
    
def WriteColorText(s,fcolor,bcolor,swap=False):
    s=s+(' ' * (80-len(s)))
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    oldColor=hWnd.GetConsoleScreenBufferInfo()['Attributes']
    newColor=(bcolor<<4)|fcolor
    if swap==True:
        #newColor=newColor^0xFF
        newColor=(fcolor<<4)|bcolor
    hWnd.SetConsoleTextAttribute(newColor)
    #print s
    hWnd.WriteConsole(s)
    hWnd.SetConsoleTextAttribute(oldColor)
    
 
if __name__=='__main__':
 
    print ('*'*80)
    for x in range(10):
        s='hello world'
        s1='this is another world'
        s= s+ ' '* (80-len(s))
        s1=s1+' '* (80-len(s1))
        WriteColorText(s,14,3,False)
        WriteColorText(s1,14,3,True)
    print ('*'*80)
    print('clear screen')
    time.sleep(2)
 




 