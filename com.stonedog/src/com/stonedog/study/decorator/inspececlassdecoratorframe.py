'''
Created on 2013-2-12

@author: Administrator
'''
from printframe import printframe

def decorator(cls):
    class wrapperclass():
        def __init__(self,*args,**kwargs):
            printframe()
            self.wrapped=cls(*args,**kwargs)
        
        def __getattr__(self,name):
            printframe()
            return getattr(self.wrapped,name)
    return wrapperclass

@decorator
class A():
    def __init__(self):
        pass
    def say(self):
        print 'hello world'
@decorator
class B():
    def __init__(self):
        self.a=A()
    
    def say(self):
        self.a.say()
        print 'hello python'

a=A()
a.say()

print(' *~* ' * 20)

b=B()
b.say()