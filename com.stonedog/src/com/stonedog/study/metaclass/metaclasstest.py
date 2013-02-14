'''
Created on 2013-2-12

@author: Administrator
'''
class Metaclass(type):
    def __new__(typeclass,classname,superclass,classdict):
        print(type(typeclass))        
        return type.__new__(typeclass,classname,superclass,classdict)

class Test():
    __metaclass__=Metaclass
    
    def __init__(self):
        pass
    
    def aha(self):
        print ('hello world')
    
a=Test()
a.aha()

def TraceDecorator(func):
    def wrapper(*args,**kwargs):
        print ('%s is Called' %(func.__name__))
        return func(*args,**kwargs)
    return wrapper

def ConfigTraceDecorator(name,trace):
    def realDecorator(func):
        def wrapper(*args,**kwargs):
            if trace==True:
                print ('%s.%s is Called' %(name,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return realDecorator

from types import FunctionType
class TraceMetaClass(type):
    def __new__(typeclass,classname,superclassname,classdict):
        for key,value in classdict.items():
            if type(value) is FunctionType:
                classdict[key]=TraceDecorator(value)
        return type.__new__(typeclass,classname,superclassname,classdict)

class ConfigTraceMetaClass(type):
    def __new__(typeclass,classname,superclass,classdict):
        if __debug__:
            for key,value in classdict.items():
                if type(value) is FunctionType:
                    classdict[key]=ConfigTraceDecorator(classname, True)(value)
        return type.__new__(typeclass,classname,superclass,classdict)
    
class Person(object):
    __metaclass__=TraceMetaClass
    
    def __init__(self,name):
        self.__name=name
    def SayHello(self):
        print self.__name

class Student(object):
    __metaclass__=ConfigTraceMetaClass
    def __init__(self,name):
        self.__name=name
    def SayHello(self):
        print 'hello world2'
p=Person('zhang')
p.SayHello()

s=Student('jiao')
s.SayHello()