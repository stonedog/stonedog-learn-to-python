'''
Created on 2013-2-11

@author: Administrator
'''
def pseudecorator(header,footer):
    #somecode
    def decorator(func):
        def wrapper(*args,**kwargs):
            wrapper.calls+=1
            print ('%s %s is called %d times %s' %(header,func.__name__,wrapper.calls,footer))
            return func(*args,**kwargs)
        wrapper.calls=0
        return wrapper
    return decorator

@pseudecorator('[Function]','[Trace]')
def test(x,y):
    print x,y

class A():
    @pseudecorator('[Class]','[Trace2]')
    def __init__(self,x,y):
        self._x=x
        self._y=y
    @pseudecorator('[Class.Method]','[Trace3]')
    def aha(self):
        print self._x,self._y

test('hello','world')
test('hello','python')

a=A('hello','java')
a.aha()
a.aha()