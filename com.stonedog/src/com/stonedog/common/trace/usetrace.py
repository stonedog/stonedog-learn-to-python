'''
Created on 2013-2-8
this is a test
@author: Administrator
'''
from trace import debug

def thisIsFunctionA():
    debug()
    
class A():
    def __init__(self):
        debug()
    
    def Aha(self):
        debug()

class B(A):
    def __init__(self):
        debug()
    def Ahb(self):
        debug()

    def Ahbb(self):
        thisIsFunctionA()

thisIsFunctionA()

print ('*'*40)
a=A()
print ('*'*40)
a.Aha()

b=B()
print ('*'*40)
b.Ahb()
print ('*'*40)
b.Ahbb()
print ('*'*40)