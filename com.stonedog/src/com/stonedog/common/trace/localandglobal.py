'''
Created on 2013-2-9

@author: Administrator
'''
class A():
    def __init__(self):
        print(locals())
    
    def Aha(self,s):
        s1=s
        print(locals())
    
    @staticmethod
    def AB():
        print (locals())
        print (globals())

        
#a=A()
#a.Aha('ba')
A.AB()
print(locals())