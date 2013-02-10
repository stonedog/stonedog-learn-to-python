#encoding=utf-8
'''
Created on 2013-2-7

@author: Administrator
'''
from stonedog.monitor.common.properties import PropertyProxy
from stonedog.monitor.common.trace import trace
class OSState(object):
    '''
    classdocs
    '''
    trace()
    HostName=PropertyProxy('HostName',str)
    DiskSpaceUsage=PropertyProxy('DiskspaceUsage',list)
    CheckTime=PropertyProxy('CheckTime',str)
    Version=PropertyProxy('Version',str)


    def __init__(self):
        '''
        Constructor
        '''
        pass

class OracleDBState(object):
    trace()
    TNSName=PropertyProxy('TNSname',str)
    ServiceName=PropertyProxy('ServiceName',str)
    DGRole=PropertyProxy('DGRole',str)
    TSSpaceUsage=PropertyProxy('TSSpaceUsage',list)
    ASMDGSpaceUsage=PropertyProxy('ASMDGSpaceUsage',list)
    Version=PropertyProxy('Version',str)
    CheckTime=PropertyProxy('CheckTime',str)
    
    def __init__(self):
        pass
    
        