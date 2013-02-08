'''
Created on 2013-2-8

@author: Administrator
'''
import sys
def get_functionname():
    print sys._getframe().f_code.co_name
    
def test():
    print sys._getframe().f_code.co_name
    get_functionname()

get_functionname()
test()


def get_funcname2():
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
        print f.f_code.co_name

def test2():
    get_funcname2()

get_funcname2()
test2()