'''
Created on 2013-2-10

@author: Administrator
'''
import inspect
def A():
    trace()
    
def trace():
    current=inspect.currentframe()
    framelist=inspect.getouterframes(current)
    for frame in framelist:
        funcName=frame[3]
        scode=frame[4]
        print str(scode).replace('\\n','').rstrip()+'in '+str(funcName)+' Was Called'
    print ('*'*40)
A()    

class TestClass():
    def __init__(self):
        trace()
    
    def Aha(self):
        trace()
    
    def AB(self):
        self.Aha()
        trace()

tobj=TestClass()
tobj.Aha()
tobj.AB()