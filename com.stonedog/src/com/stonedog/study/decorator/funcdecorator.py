'''
Created on 2013-2-11

@author: Administrator
'''
def decorator(func):
    def wrapper(*args,**kwargs):
        print (type(args[0]),args[0])
        print (func.__name__,' Is Called')
        func(*args,**kwargs)
    return wrapper

@decorator
def test(s1,s2):
    print (s1,s2)

test('hello','world ')

class A():
    @decorator
    def __init__(self):
        pass
    
    @decorator
    def aha(self,s1,s2):
        print s1,s2

a=A()
a.aha('hell0 ','world')
    