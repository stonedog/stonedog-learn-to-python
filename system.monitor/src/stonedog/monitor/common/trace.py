#encoding=utf-8
'''
Created on 2013-2-10

@author: Administrator
'''
import sys,traceback


def trace():
    stacks=traceback.extract_stack(sys._getframe())
    header='--'*(len(stacks)-3)
    print ('%s : In File : [%s]' %(header+stacks[-3][3],stacks[-3][0]))

'''
栈视图

|---------------------------|
| .... other function       |
|---------------------------|
|somefunction               |
| call trace()              | 
|---------------------------|
|trace                      |
|---------------------------|
|traceback.extract_stack()  |
----------------------------|
'''    


 
 