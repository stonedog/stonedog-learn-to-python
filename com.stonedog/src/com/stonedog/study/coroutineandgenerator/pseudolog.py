'''
Created on 2013-2-17

@author: Administrator
'''
import time 
f=open('d:/test.log','a')
for i in xrange(10000):
    f.write('this is a log %d\n' % i)
    f.flush()
    time.sleep(1)
f.close()