#encoding=utf-8
'''
Created on 2013-2-2

@author: Administrator
'''
import subprocess
class WindowsConsole():
    @staticmethod
    def CreateConsole():
        con=subprocess.Popen('pythonw showdata.py',stdin=subprocess.PIPE)
        return WindowsConsole(con)
    
    def __init__(self,con):
        self.__con=con
    
    def ShowData(self,data):
        self.__con.stdin.write(data+'\n')
    
    def KillWindow(self):
        self.__con.terminate()

if __name__=='__main__':
    l_flag=True
    win1=None
    while l_flag:
        print(u'请输入：c:打开新窗口 x--退出 1--发送数据 2--关闭窗口')
        
        ch=raw_input()
        if ch=='X':
            l_flag=False
        elif ch=='c':
            win1=WindowsConsole.CreateConsole()     
            print(ch)
        elif ch=='1':
            datas=raw_input()
            win1.ShowData(datas)
        elif ch=='2':
            win1.KillWindow()
            
            