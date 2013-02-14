'''
Created on 2013-2-12

@author: Administrator
'''
from printframe import printframe

def Decorator(fun):
    def wrapper(*args,**kwargs):
        printframe()
        return fun(*args,**kwargs)
    return wrapper

def pseuDecorator(header,footer,trace):
    def realDecorator(fun):
        if trace==False:
            return fun
        else:
            def wrapper(*args,**kwargs):
                printframe()
                return fun(*args,**kwargs)
            return wrapper
    return realDecorator
#@Decorator
@pseuDecorator('[]','[]',True)
def funcTest():
    pass

class A():
    def __init__(self):
        pass
    
    @pseuDecorator('[]','[]',True)
    def aha(self):
        print ('hello world')

funcTest()
a=A()
a.aha()