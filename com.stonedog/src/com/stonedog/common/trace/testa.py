'''
Created on 2013-2-10

@author: Administrator
'''
import sys,inspect,traceback
def trace():
    frame=sys._getframe()
   
    traces=traceback.extract_stack(frame)
    print(type(traces))
    for i in traces:
        print ('*'*100) 
        for j in i:
            print type(j),j
        

    frame2=inspect.currentframe()
    
    print (frame==frame2)
'''
    print('form here -------------------')
    framelist=inspect.getouterframes(frame)
    print ('-'*80)
    for f in framelist:
        print type(f)
        print (frame==f[0])
        for i in f:
            print i,type(i)
        
        print ('*'*80)
     '''    
def a():
    trace()
def b():
    a()
a()
print('-'*100)

       