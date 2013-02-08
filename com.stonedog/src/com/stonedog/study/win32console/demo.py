#encoding=utf-8
'''
Created on 2013-2-2

@author: Administrator
'''

import win32console, win32con
import traceback, time

virtual_keys={}
for k,v in win32con.__dict__.items():
    if k.startswith('VK_'):
        virtual_keys[v]=k 

free_console=True
try:
    win32console.AllocConsole()
    print('get conole')
    time.sleep(1)
except win32console.error, err_tuple:
    print('here')
    time.sleep(1)
    if err_tuple[0]!=5:
        raise
    ## only free console if one was created successfully
    free_console=False
win32console.SetConsoleTitle(u'这个窗口好看吗')
try:
    stdout=win32console.GetStdHandle(win32console.STD_OUTPUT_HANDLE)
    win32console.SetConsoleTitle('geted')
except Exception,data:
    win32console.SetConsoleTitle('did not get')

stdin=win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)

newbuffer=win32console.CreateConsoleScreenBuffer()
newbuffer.SetConsoleActiveScreenBuffer()
newbuffer.SetConsoleTextAttribute(win32console.FOREGROUND_RED|win32console.FOREGROUND_INTENSITY
        |win32console.BACKGROUND_GREEN|win32console.BACKGROUND_INTENSITY)
newbuffer.WriteConsole('This is a new screen buffer\n')

## test setting screen buffer and window size
## screen buffer size cannot be smaller than window size
window_size=newbuffer.GetConsoleScreenBufferInfo()['Window']

coord=win32console.PyCOORDType(X=window_size.Right+20, Y=window_size.Bottom+20)
newbuffer.SetConsoleScreenBufferSize(coord)

window_size.Right+=10
window_size.Bottom+=10
#newbuffer.SetConsoleWindowInfo(Absolute=True,ConsoleWindow=window_size)

## write some records to the input queue 
x=win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
x.Char=u'X'
x.KeyDown=True
x.RepeatCount=1
x.VirtualKeyCode=0x58
x.ControlKeyState=win32con.SHIFT_PRESSED

z=win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
z.Char=u'Z'
z.KeyDown=True
z.RepeatCount=1
z.VirtualKeyCode=0x5a
z.ControlKeyState=win32con.SHIFT_PRESSED

 

#stdin.WriteConsoleInput([x,z,x])

newbuffer.SetConsoleTextAttribute(win32console.FOREGROUND_RED|win32console.FOREGROUND_INTENSITY
        |win32console.BACKGROUND_GREEN|win32console.BACKGROUND_INTENSITY)
newbuffer.WriteConsole('Press some keys, click some characters with the mouse\n')

newbuffer.SetConsoleTextAttribute(win32console.FOREGROUND_BLUE|win32console.FOREGROUND_INTENSITY
        |win32console.BACKGROUND_RED|win32console.BACKGROUND_INTENSITY)
newbuffer.WriteConsole('Hit "End" key to quit\n')
                    
breakout=False
while not breakout:
    newbuffer.WriteConsole('pao dao zhe li le \n')
    time.sleep(3)    
    input_records=stdin.ReadConsoleInput(10)

    for input_record in input_records:
        if input_record.EventType==win32console.KEY_EVENT:
            if input_record.KeyDown:
                if input_record.Char=='\0':
                    newbuffer.WriteConsole(virtual_keys.get(input_record.VirtualKeyCode, 'VirtualKeyCode: %s' %input_record.VirtualKeyCode))
                else:
                    newbuffer.WriteConsole(input_record.Char)
                if input_record.VirtualKeyCode==win32con.VK_END:
                    breakout=True
                    break
        elif input_record.EventType==win32console.MOUSE_EVENT:
            if input_record.EventFlags==0:  ## 0 indicates a button event
                if input_record.ButtonState!=0:   ## exclude button releases
                    pos=input_record.MousePosition
                    # switch the foreground and background colors of the character that was clicked
                    attr=newbuffer.ReadConsoleOutputAttribute(Length=1, ReadCoord=pos)[0]
                    new_attr=attr
                    if attr&win32console.FOREGROUND_BLUE:
                        new_attr=(new_attr&~win32console.FOREGROUND_BLUE)|win32console.BACKGROUND_BLUE
                    if attr&win32console.FOREGROUND_RED:
                        new_attr=(new_attr&~win32console.FOREGROUND_RED)|win32console.BACKGROUND_RED
                    if attr&win32console.FOREGROUND_GREEN:
                        new_attr=(new_attr&~win32console.FOREGROUND_GREEN)|win32console.BACKGROUND_GREEN

                    if attr&win32console.BACKGROUND_BLUE:
                        new_attr=(new_attr&~win32console.BACKGROUND_BLUE)|win32console.FOREGROUND_BLUE
                    if attr&win32console.BACKGROUND_RED:
                        new_attr=(new_attr&~win32console.BACKGROUND_RED)|win32console.FOREGROUND_RED
                    if attr&win32console.BACKGROUND_GREEN:
                        new_attr=(new_attr&~win32console.BACKGROUND_GREEN)|win32console.FOREGROUND_GREEN
                    newbuffer.WriteConsoleOutputAttribute((new_attr,),pos)
        else:
            newbuffer.WriteConsole(str(input_record))
    time.sleep(0.1)

stdout.SetConsoleActiveScreenBuffer()
newbuffer.Close()
if free_console:
     win32console.FreeConsole()
