'''
Created on 2013-2-11

@author: Administrator
'''
def statedecorator(fun):
    def wrapper(*args,**kwargs):
        wrapper.calls+=1
        print ('%s is called %d times' %(fun.__name__,wrapper.calls))
        return fun(*args,**kwargs)
    wrapper.calls=0
    return wrapper

@statedecorator
def test(x,y):
    print (x,y)

class A():
    @statedecorator
    def __init__(self,x,y):
        self._x=x
        self._y=y
    
    @statedecorator
    def aha(self):
        print (self._x,self._y)

test('hello ','world')
a=A('hello','python')
a.aha()
test('hello','python')
a.aha()