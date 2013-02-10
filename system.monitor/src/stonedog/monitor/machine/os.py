'''
Created on 2013-2-7

@author: Administrator
'''
from abstractcomponent import AbstractMachineComponent
from state import OSState
from stonedog.monitor.common.trace import trace
class XNixOS(AbstractMachineComponent):
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
    
    def CheckDiskSpace(self):
        trace()
        return []
    
    def CheckAll(self):
        trace()
        osState=OSState()
        
        osState.Version=self.CheckVersion()
        osState.DiskSpaceUsage=self.CheckDiskSpace()
        osState.HostName=''
        osState.CheckTime=''
        return osState
        