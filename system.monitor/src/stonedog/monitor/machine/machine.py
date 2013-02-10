'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.common.trace import trace
from stonedog.monitor.machine.db import OracleDB
from stonedog.monitor.machine.os import XNixOS
class OneServerMachine(object):
    '''
    classdocs
    '''
    def __init__(self,machineConfig):
        '''
        Constructor
        '''
        trace()
        self._components={'OS':XNixOS(machineConfig),'DB':OracleDB(machineConfig)}
        self._machineState={'OS':None,'DB':None}
        self._machineConfig=machineConfig
    
    def CheckAll(self):
        trace()
        for key,component in self._components.items():
            if component:
                self._machineState[key]=component.CheckAll()
        
        return self._machineState    
    
            
        
        
    
    
        