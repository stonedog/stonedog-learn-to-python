'''
Created on 2013-2-12

@author: Administrator
'''
from printframe import printframe
def ConfigDecorator(header,footer):
    def realDecorator(func):
        if __debug__:
            def wrapper(*args,**kwargs):
                print(header)
                printframe()
                print(footer)
                return func(*args,**kwargs)
            return wrapper
        else :
            return func
    return realDecorator
''' Test Case
@ConfigDecorator('[Begin]','[End]')
def test(x,y):
    print x,y

class A():
    @ConfigDecorator('[Begin]','[End]')
    def __init__(self):
        self._x='hello'
        self._y='python'
    @ConfigDecorator('[Begin]','[End]')
    def say(self):
        test(self._x,self._y)

test('hello','world')
a=A()
a.say()
'''
from types import FunctionType
def ConfigMetaDecorator(header,footer):
    class ConfigMetaClass(type):
        def __new__(typeclass,classname,superclassname,classdict):
            for key,value in classdict.items():
                if type(value) is FunctionType:
                    if __debug__:
                        classdict[key]=ConfigDecorator(header,footer)(value)
            return type.__new__(typeclass,classname,superclassname,classdict)
    return ConfigMetaClass

class Person(object):
    __metaclass__=ConfigMetaDecorator('[Begin]','[End]')
    def __init__(self,name):
        self.__name=name
    def say(self):
        print (self.__name)

p=Person('zhang')
p.say()
    
    
    
    