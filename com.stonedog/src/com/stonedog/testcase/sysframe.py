'''
Created on 2013-2-8

@author: Administrator
'''
import sys,inspect
def get_functionname():
    print sys._getframe().f_code.co_name
    
def test():
    print sys._getframe().f_code.co_name
    get_functionname()

#get_functionname()
#test()


def get_funcname2():
    try:
        raise Exception
    except:
        f1 = sys.exc_info()[2].tb_frame
        print(type(f1))
        f=f1.f_back
        f2=f.f_back
        print f.f_code.co_name
        print(type(f))
        print(inspect.getframeinfo(f)[3])
        if f2 is not None:
            print(inspect.getframeinfo(f2)[3])
    print ('*'*80)
        

def test2():
    get_funcname2()

get_funcname2()
test2()