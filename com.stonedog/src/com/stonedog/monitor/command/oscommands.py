#encoding=utf-8
'''
Created on 2013-1-27

@author: Administrator
'''
from basecommand import CommandObject

class OSDsikCommand(CommandObject):
    def __init__(self,p_machine):
        self.__machine=p_machine
    
    def Execute(self):
        self.__machine.GetDiskUsage()

class OSInfoCommand(CommandObject):
    def __init__(self,p_machine):
        self.__machine=p_machine
    
    def Execute(self):
        self.__machine.GetHostInfo()
                