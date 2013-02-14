'''
Created on 2013-2-10

@author: Administrator
'''
import inspect,traceback
def traceuseinspce():
    current=inspect.currentframe()
    framelist=inspect.getouterframes(current)
    print len(framelist)
    for frame in framelist:
        funcName=frame[3]
        scode=frame[4]
        print str(scode).replace('\\n','').rstrip()+'in '+str(funcName)+' Was Called'
    print ('*'*40)

def traceusestack():
    current=inspect.currentframe()
    stacks=traceback.extract_stack(current)
    print len(stacks)
    
    for i in stacks:
        print i[3]

def A():
    traceuseinspce()
def B():
    traceusestack()    
A()
B()

def C():
    traceuseinspce()
    A()
def D():
    traceuseinspce()
    C()    
 
 
'''
class TestClass():
    def __init__(self):
        trace()
    
    def Aha(self):
        trace()
    
    def AB(self):
        self.Aha()
        trace()

tobj=TestClass()
 '''