#encoding=utf-8
'''
Created on 2013-2-5

@author: Administrator
'''
import win32console
import time
 
#time.sleep(3)

def setConsoleWindowSizeTest():
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    print (hWnd)
    
    windowMaxSize=hWnd.GetConsoleScreenBufferInfo()['MaximumWindowSize']

    widthLimit=windowMaxSize.X
    heightLimit=windowMaxSize.Y
    
    for x in range(widthLimit):
        for y in range(heightLimit):
            newWindowSize=win32console.PySMALL_RECTType(Left=0,Top=0,Right=x,Bottom=y)
            hWnd.SetConsoleWindowInfo(Absolute=True,ConsoleWindow=newWindowSize)
            
            print hWnd.GetConsoleScreenBufferInfo()
            time.sleep(0.01)
'''
def ChangeConsoleScreenBufferSize():
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    screenInfo=hWnd.GetConsoleScreenBufferInfo()
    print screenInfo
    screenBufferSize=screenInfo['Size']
    rows=screenBufferSize.X
    cols=screenBufferSize.Y
    
    
    rows+=10
    cols+=20
    
    newSize=win32console.PyCOORDType(X=rows,Y=cols)
    
    hWnd.SetConsoleScreenBufferSize(newSize)
    
    newScreenInfo=hWnd.GetConsoleScreenBufferInfo()
    
    print ('*' * 60)
    print newScreenInfo
'''
#ChangeConsoleScreenBufferSize()

def ChangeConsoleWindowSize(width,height):
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
  
    newWindowSize=win32console.PySMALL_RECTType(Left=0,Top=0,Right=width,Bottom=height)
    hWnd.SetConsoleWindowInfo(Absolute=True,ConsoleWindow=newWindowSize)

def ChangeConsoleScreenBufferSize(width,height):
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    print hWnd.GetConsoleScreenBufferInfo()
    newSize=win32console.PyCOORDType(X=width,Y=height)
    
    hWnd.SetConsoleScreenBufferSize(newSize)
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
    
def ClearScreen():
    hWnd=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    screenBufferInfo=hWnd.GetConsoleScreenBufferInfo()
    fillColor=screenBufferInfo['Attributes']
    screenSize=screenBufferInfo['Size']
    coord=win32console.PyCOORDType(X=0,Y=0)
    
    hWnd.FillConsoleOutputCharacter(u' ',screenSize.X*screenSize.Y,coord)
    
    
    time.sleep(6)
    
    hWnd.FillConsoleOutputAttribute(fillColor,screenSize.X*screenSize.Y,coord)
    time.sleep(6)
    hWnd.SetConsoleCursorPosition(coord)
    
'''
print方法，会在每个字符串后面自动加一个回车换行，因此，如果s恰好是80个字符，最终
在屏幕上会占据两行，第一行是s，第二行其实是回车换行
但如果s是79个字符，又会在每行最后留下一个空白。

而WriteConsole就没有这个问题。
'''  
if __name__=='__main__':
    ChangeConsoleScreenBufferSize(80,400)
    ChangeConsoleWindowSize(79,40)
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
    #ClearScreen()




 