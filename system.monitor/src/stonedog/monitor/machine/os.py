'''
Created on 2013-2-7

@author: Administrator
'''
from abstractcomponent import AbstractMachineComponent
from state import OSState
class XNixOS(AbstractMachineComponent):
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
    
    def CheckDiskSpace(self):
        pass
    
    def CheckAll(self):
        osState=OSState()
        
        osState.Version=self.CheckVersion()
        osState.DiskSpaceUsage=self.CheckDiskSpace()
        osState.HostName=''
        osState.CheckTime=''
        return osState
        