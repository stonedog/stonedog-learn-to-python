'''
Created on 2013-2-7

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