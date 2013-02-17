'''
Created on 2013-2-17

@author: Administrator
'''
import time

from conroutine import coroutine

def source(t):
    f=open('d:/test.log','r')
    f.seek(0,2)
    while True:
        line=f.readline()
        if not line:
            time.sleep(0.1)
            continue
        t.send(line)

@coroutine
def printer():
    while True:
        line=(yield)
        print line

@coroutine
def grep(pattern,target):
    print 'in grep'
    while True:
        line=(yield)
        if pattern in line:
            target.send(line)

source(grep('43',printer()))

 
    