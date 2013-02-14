'''
Created on 2013-2-11

@author: Administrator
'''
def decorator(cls):
    class wrapper():
        def __init__(self,*args,**kwargs):
            print cls.__name__,'.__init__ is called'
            self.wraped=cls(*args,**kwargs)
        def __getattr__(self,name):
            print '%s.%s is called' %(cls.__name__,name)
            return getattr(self.wraped,name)
    return wrapper

@decorator
class A():
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    def aha(self):
        print self._x,self._y

a=A('hello','world')
a.aha()