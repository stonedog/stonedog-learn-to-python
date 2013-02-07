'''
Created on 2013-2-7

@author: Administrator
'''

class AbstractMachineComponent(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        raise NotImplementedError('AbstractMachineComponent')
    
    def CheckALL(self):
        raise NotImplementedError('CheckAll')
    
    def CheckVersion(self):
        raise NotImplementedError('CheckVersion')
    
    def Connect(self):
        raise NotImplementedError('Connect')
    
    def Close(self):
        raise NotImplementedError('Close')
    