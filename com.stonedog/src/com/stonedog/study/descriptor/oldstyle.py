'''
Created on 2013-2-3

@author: Administrator
'''
class DBState():
    def __init__(self):
        self.__tns=''
        self.__hostname=''
        self.__servicename=''
    
    @property
    def TNS(self):
        return self.__tns
    
    @TNS.setter
    def TNS(self,tns):
        self.__tns=tns
        
    @property
    def HostName(self):
        return self.__hostname
    
    @HostName.setter
    def HostName(self,hostname):
        self.__hostname=hostname
        
    @property
    def ServiceName(self):
        return self.__servicename
    
    @ServiceName.setter
    def ServiceName(self,servicename):
        self.__servicename=servicename

if __name__=='__main__':
    dbState=DBState()
    dbState.TNS='testdb'
    dbState.HostName='192.168.1.1'
    
    print dbState.TNS