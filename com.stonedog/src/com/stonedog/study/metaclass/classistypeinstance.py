'''
Created on 2013-2-12
class is type instance
@author: Administrator
'''
class A():
    def __init__(self):
        pass

class B(object):
    def __init__(self):
        pass

print (type(A))
print (type(type(A)))
print (type(B))
print(type(object))


a=[]
b=()
c={}
d=''

print (type(a))
print (type(b))
print (type(c))
print (type(d))

print type(type(a))
print type(type(b))
print type(type(c))
print type(type(d))

class C(object):
    pass
c=C()
print c.__class__
print C.__class__