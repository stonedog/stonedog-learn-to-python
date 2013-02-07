'''
Created on 2013-2-7

@author: Administrator
'''

class OneServerMachine(object):
    '''
    classdocs
    '''
    def __init__(self,machineConfig):
        '''
        Constructor
        '''
        self._components={'OS':None,'DB':None}
        self._machineState={'OS':None,'DB':None}
        self._machineConfig=machineConfig
    
    def CheckAll(self):
        for key,component in self._components.items:
            if component:
                self._machineState[key]=component.CheckAll(self._machineConfig)
        
        return self._machineState    
    
            
        
        
    
    
        