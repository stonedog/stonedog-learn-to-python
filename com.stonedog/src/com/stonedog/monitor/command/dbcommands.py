#encoding=utf-8
'''
Created on 2013-1-27

@author: Administrator
'''
from basecommand import CommandObject

class DBTSCommand(CommandObject):
    '''
    表空间使用情况
    '''
    def __init__(self,p_db):
        self.__db=p_db
        
    def Execute(self):
        return self.__db.CheckTSUsage()


class DBAASCommand(CommandObject):
    def __init__(self,p_db):
        self.__db=p_db
    
    def Execute(self):
        return self.__db.CheckAAS()

class DBASMDGCommand(CommandObject):
    def __init__(self,p_db):
        self.__db=p_db
    def Execute(self):
        return self.__db.CheckASMDG()    
    
            