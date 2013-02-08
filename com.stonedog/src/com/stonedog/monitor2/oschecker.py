'''
Created on 2013-2-6

@author: Administrator
'''
from com.stonedog.common.os.linuxos import XNixHost
from com.stonedog.common.config.initconfig import ConfigObject

class XNixHostCheckerFactory():
    @staticmethod
    def GetHostChecker(cf):
        return LinuxOSChecker(cf)
    
class LinuxOSChecker():
    def __init__(self,cf):
        self._cf=cf
        self._host=XNixHost(cf)
          
    def Check(self):
        disks=self._host.CheckDisk() 
        return disks  
