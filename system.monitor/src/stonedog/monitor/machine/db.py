'''
Created on 2013-2-7

@author: Administrator
'''
from abstractcomponent import AbstractMachineComponent
from state import OracleDBState
from stonedog.monitor.common.trace import trace
class OracleDB(object):
    '''
    classdocs
    '''
    def __init__(self,machineConfig):
        '''
        Constructor
        '''
        trace()
        self._machineConfig=machineConfig
        self.Connect()
        
    def Connect(self):
        trace()
    
    def Close(self):
        trace()
    
    def CheckVersion(self):
        trace()
        return ''
    
    def CheckTSSpaceUsage(self):
        trace()
        return []
    def CheckASMDGSpaceUsage(self):
        trace()
        return []
    
    def CheckDGRole(self):
        trace()
        return ''
    
    def CheckAll(self):
        trace()
        
        dbState=OracleDBState()
        
        dbState.Version=self.CheckVersion()
        dbState.CheckTime=''
        #if self._machineConfig.HaveASM=='True':
        dbState.ASMDGSpaceUsage=self.CheckASMDGSpaceUsage()
        dbState.DGRole=self.CheckDGRole()
        dbState.TSSpaceUsage=self.CheckTSSpaceUsage()
        return dbState