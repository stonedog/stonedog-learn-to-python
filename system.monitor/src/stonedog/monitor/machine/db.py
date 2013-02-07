'''
Created on 2013-2-7

@author: Administrator
'''
from abstractcomponent import AbstractMachineComponent
from state import OracleDBState
class OracleDB(object):
    '''
    classdocs
    '''
    def __init__(self,machineConfig):
        '''
        Constructor
        '''
        self._machineConfig=machineConfig
        self.Connect()
        
    def Connect(self):
        pass
    
    def Close(self):
        pass
    
    def CheckVersion(self):
        pass
    
    def CheckTSSpaceUsage(self):
        pass
    
    def CheckASMDGSpaceUsage(self):
        pass
    
    def CheckDGRole(self):
        pass
    
    def CheckAll(self):
        dbState=OracleDBState()
        
        dbState.Version=self.CheckVersion()
        dbState.CheckTime=''
        if self._cf.HaveASM=='True':
            dbState.ASMDGSpaceUsage=self.CheckASMDGSpaceUsage()
        dbState.DGRole=self.CheckDGRole()
        dbState.TSSpaceUsage=self.CheckTSSpaceUsage()
        return dbState