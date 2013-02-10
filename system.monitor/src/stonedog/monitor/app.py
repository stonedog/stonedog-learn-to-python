#encoding=utf-8
'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.common.trace import trace
from stonedog.monitor.checker.machinechecker import OneMachineChecker
class Application(object):
    
    def __init__(self,fileName):
        trace()
        self.__configFile=fileName
        self._configs=['0']

    def InitConfig(self):
        trace()
    
    def CheckAllMachine(self):
        trace()
        for cf in self._configs :
            self.CheckOneMachine(cf)
    
    def CheckOneMachine(self,cf):
        trace()
        oneChecker=OneMachineChecker(cf)
        oneChecker.CheckAndReport()
  
if __name__=='__main__':
    app=Application('d:\host.conf')
    app.InitConfig()
    app.CheckAllMachine()
            
        
    

