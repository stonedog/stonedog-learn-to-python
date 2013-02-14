'''
Created on 2013-2-12

@author: Administrator
'''
from abc import ABCMeta,abstractmethod

class db(object):
    __metaclass__=ABCMeta
    
    def __init__(self):
        self._type='DB'
    @abstractmethod
    def open(self):
        pass
    
    @abstractmethod
    def close(self):
        pass

    def __str__(self):
        return self._type

class OracleDB(db):
    def __init__(self):
        pass
    
    def open(self):
        print 'connect to database'
    def close(self):
        print 'close database'

test=db()

test=OracleDB()
test.open()    