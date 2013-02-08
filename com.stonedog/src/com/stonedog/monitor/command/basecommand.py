#encoding=utf-8
class CommandObject(object):
    def __init__(self,p_executer):
        self.__executer=p_executer
        
    def Execute(self,**args):
        pass