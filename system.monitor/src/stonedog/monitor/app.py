#encoding=utf-8
'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.checker.machinechecker import OneMachineChecker
class Application(object):
    
    def __init__(self,fileName):
        self.__configFile=fileName
        self._configs=[]
        
    def InitConfig(self):
        pass
    
    def CheckAllMachine(self):
        for cf in self._config :
            self.CheckOneMachine(cf)
    
    def CheckOneMachine(self,cf):
        oneChecker=OneMachineChecker(cf)
        oneChecker.CheckAndReport()
  
if __name__=='__main__':
      app=Application('d:\host.conf')
      app.CheckAllMachine()
            
        
    

