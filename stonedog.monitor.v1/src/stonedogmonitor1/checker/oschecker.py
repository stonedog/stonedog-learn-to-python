'''
Created on 2013-2-16

@author: Administrator
'''
from stonedogmonitor1.os.xnixos import XNixHost
 
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
