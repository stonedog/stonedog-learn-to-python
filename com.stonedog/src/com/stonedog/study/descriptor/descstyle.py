'''
Created on 2013-2-3

@author: Administrator
'''

class PropertyProxy(object):
    '''
    classdocs
    '''
    def __init__(self,propname,proptype,default=None):
        self.name='_'+propname
        self.type=proptype
        self.default_value=default if default else proptype()
    def __get__(self,instance,cls):
        return getattr(instance,self.name,self.default_value)
    def __set__(self,instance,value):
        if not isinstance(value,self.type):
            raise TypeError('must by %s type' % self.type)
        setattr(instance,self.name,value)
    def __delete__(self,instance):
        raise AttributeError('can not delete attribute')

class DBState():
    TNS=PropertyProxy('TNS',str)
    HostName=PropertyProxy('HostName',str)
    ServiceName=PropertyProxy('ServiceName',str)
    def __init__(self):
        pass
    
if __name__=='__main__':
    dbState=DBState()
    dbState.TNS='testdb'
    dbState.HostName='192.168.1.1'        
    dbS2=DBState()
    dbS2.TNS='testdb2'
    
    print dbState.TNS
    print dbS2.TNS
    print dbState.TNS
        