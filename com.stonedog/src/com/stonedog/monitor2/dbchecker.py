#encoding=utf-8
'''
Created on 2013-1-31

@author: Administrator
'''
from com.stonedog.common.db.oracledb import OracleDB,DBState
from com.stonedog.common.config.initconfig import ConfigObject

class OracleDBCheckerFactory(object):
    @staticmethod
    def GetDBChecker(cf):
        if cf.ASMTNS=='':
            return OracleRDBMSChecker(cf)
        else :
            return OracleASMChecker(cf)
        

class OracleRDBMSChecker(object):
    def __init__(self,cf):
        self._cf=cf
        self._db=OracleDB(cf)
        
    def Check(self):
        dbstate=DBState()
        dbstate.HostName=self._cf.HostName
        dbstate.TNS=self._cf.TNS
        dbstate.ServiceName=self._cf.ServiceName
        
        dbstate.Status=self._db.CheckStatus()
        dbstate.Version=self._db.CheckVersion()
        dbstate.TSUsage=self._db.CheckTSUsage()
        dbstate.AAS=self._db.CheckAAS()
        
        return dbstate

class OracleASMChecker(OracleRDBMSChecker):
    def __init__(self,cf):
        super(OracleASMChecker,self).__init__(cf)
    
    def Check(self):
        dbstate=super(OracleASMChecker,self).Check()
        dbstate.ASMDG=self._db.CheckASMDG()
        
        return dbstate
    

if __name__=='__main__':
    cf=ConfigObject()
    #cf.ASMTNS='ASM_192.168.1.26'
    cf.HostName='192.168.1.26'
    cf.ServiceName='wxxrdb.center.wxxr.com.cn'
    
    dbc=OracleRDBMSChecker(cf)
    print dbc.Check()      

    print ('-'*30)
    
    asdbc=OracleASMChecker(cf)
    print asdbc.Check()
       
        
        
