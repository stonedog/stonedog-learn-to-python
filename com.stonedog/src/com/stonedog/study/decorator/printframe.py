'''
Created on 2013-2-12

@author: Administrator
'''
import inspect
def printframe():
    current=inspect.currentframe()
    framelist=inspect.getouterframes(current)
    for oneframe in framelist:
        print ('%s in %s is called' %(oneframe[3],oneframe[4]))
    print ('~'*100)
def c():
    printframe()



class A():
    def aha(self):
        printframe()
if __name__=='__main__':
    c()
    a=A()
    a.aha()


