'''
Created on 2013-2-17

@author: Administrator
'''
def coroutine(func):
    def wrapper(*args,**kwargs):
        print('first calles')
        cr=func(*args,**kwargs)
        cr.next()
        return cr
    return wrapper

@coroutine
def grep(pattern):
    print 'hello'
    while True:
        line=(yield)
        if pattern in line:
            print (line)
        
 
g=grep('abc')
print(type(g))
g.send('hello abc')
g.send('hello abc2')
