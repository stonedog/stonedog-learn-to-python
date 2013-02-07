#encoding=utf-8
'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.common.properties import PropertyProxy
class MachineConfig(object):
    '''
    classdocs
    '''
    HostName=PropertyProxy('HostName',str)
    HaveDB=PropertyProxy('HaveDB',str)
    HaveASM=PropertyProxy('HaveASM',str)
    DBServiceName=PropertyProxy('DBServiceName',str)
    DBTNSName=PropertyProxy('DBTNSName',str)
    HostUser=PropertyProxy('HostUserName',str)
    HostPassword=PropertyProxy('HostUserPassword',str)
    DBUser=PropertyProxy('DBUser',str)
    DBPassword=PropertyProxy('DBUserPassword',str)
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    @staticmethod
    def GetMachineConfig(hostname,haveDB,haveASM,dbservicename,tns,user,password,dbuser,dbpassword):
        mc=MachineConfig()
        mc.HostName=hostname
        mc.HaveDB=haveDB
        mc.DBServiceName=dbservicename
        mc.DBTNSName=tns
        mc.HostUser=user
        mc.HostPassword=password
        mc.DBUser=dbuser
        mc.DBPassword=dbpassword
        mc.HaveASM=haveASM
    
    