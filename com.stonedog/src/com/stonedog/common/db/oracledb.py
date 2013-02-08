#encoding=utf-8
import cx_Oracle
from checksql import TS_SQL,ASM_DG_SQL,VERSION_SQL
from com.stonedog.common.config.initconfig import ConfigObject
from com.stonedog.common.db.db import DB
class OracleDB(DB):
    
    TSUSAGE='Tablespace Usage'
    AAS='Average Active Session'
    ASMDG='ASM Disk Group'
    VERSION='Version'
    STATUS='Status'
    HOSTNAME='HostName'
    TNS='TNS'
    SERVICENAME='ServiceName'
    

    def __init__(self,conf_obj):
        if  isinstance(conf_obj,ConfigObject):
            #print (conf_obj.GetTNS())
            tns=conf_obj.GetTNS()
            
            self._connection=cx_Oracle.connect('sys','H2oisWater',tns,mode=cx_Oracle.SYSDBA)
            self._cursor=self._connection.cursor()
            self._cursor.execute('select status from v$instance')
            self.__status=self._cursor.fetchone()[0]
        else :
            pass

    
    def CheckStatus(self):
        return self.__status

        
    def CheckTSUsage(self):
        if self.__status=='OPEN':
            return super(OracleDB,self)._check_space(TS_SQL)
        else :
            return []


    def CheckASMDG(self):
        if self.__status=='OPEN':
            return super(OracleDB,self)._check_space(ASM_DG_SQL)
        else :
            return []
    
    def CheckAAS(self):
        '''
        Check Average Active Session
        '''
        if self.__status=='OPEN':
            l_as={'2011-1-10':'24','2011-1-11':'25'}
            return l_as
        else:
            return []
    
    def CheckVersion(self):
        self._cursor.execute(VERSION_SQL)
        l_version=[]
        row=self._cursor.fetchone()
        while row:
            l_version.append(row[0]+'\n')
            row=self._cursor.fetchone()
      
        return l_version
        
    
class DBState(object):
    def __init__(self):
        self.__dbstate={}
    '''
    __dbstate是一个字典，每个key是个字符串，每个value都是个数组，而数组的成员是元祖。
    {'version':['...',',,,',
     'TS usage'|'ASM DB':[('product','100m','80m'，'80’),(...),..],
     'AAS':[(),()],
     'Status':'OPEN|MOUNTED',
     'HostName':'..',
     'TNS':'..',
     'ServiceName':'.'
    }
    '''
    @property
    def Version(self):
        return self.__dbstate.get(OracleDB.VERSION,[])
    @Version.setter
    def Version(self,version):
        self.__dbstate[OracleDB.VERSION]=version
    
    @property
    def Status(self):
        return self.__dbstate[OracleDB.STATUS]
    @Status.setter
    def Status(self,status):
        self.__dbstate[OracleDB.STATUS]=status
        
    @property
    def TSUsage(self):
        return self.__dbstate.get(OracleDB.TSUSAGE,[])
    
    @TSUsage.setter
    def TSUsage(self,tsu):
        self.__dbstate[OracleDB.TSUSAGE]=tsu
        
    @property
    def AAS(self):
        return self.__dbstate.get(OracleDB.AAS,[])

    @AAS.setter
    def AAS(self,aas):
        self.__dbstate[OracleDB.AAS]=aas
    
    @property
    def ASMDG(self):
        return self.__dbstate.get(OracleDB.ASMDG,[])
    
    @ASMDG.setter
    def ASMDG(self,asmdg):
        self.__dbstate[OracleDB.ASMDG]=asmdg
    
    @property
    def HostName(self):
        return self.__dbstate[OracleDB.HOSTNAME]
    @HostName.setter
    def HostName(self,hostname):
        self.__dbstate[OracleDB.HOSTNAME]=hostname
    
    @property
    def TNS(self):
        return self.__dbstate[OracleDB.TNS]
    
    @TNS.setter
    def TNS(self,tns):
        self.__dbstate[OracleDB.TNS]=tns
    
    @property
    def ServiceName(self):
        return self.__dbstate[OracleDB.SERVICENAME]
    @ServiceName.setter
    def ServiceName(self,svname):
        self.__dbstate[OracleDB.SERVICENAME]=svname
        
        
    def __str__(self):
        l_s=''
        l_s += self.HostName()+':'+self.ServiceName()+':'+self.TNS()+':'+self.Status()+'\n'
        
        if self.__dbstate.has_key(OracleDB.VERSION):
            for s in self.__dbstate[OracleDB.VERSION]:
                l_s+=s 
        if self.__dbstate.has_key(OracleDB.TSUSAGE):
            l_s+='表空间使用情况：总量(G)、余量(G)\n'
            for (ts,tm,fm) in self.__dbstate[OracleDB.TSUSAGE]:
                l_s+='%10s : %10s : %10s \n'%(ts,tm,fm)
        if self.__dbstate.has_key(OracleDB.ASMDG):
            l_s+='ASM 磁盘组使用情况：总量(G)、余量(G)\n'
            for (dg,tm,fm) in self.__dbstate[OracleDB.ASMDG]:
                l_s+='%10s : %10s : %10s \n'%(dg,tm,fm)
        
        return l_s
                


if __name__=='__main__':
    cf=ConfigObject()
    #cf.ASMTNS='ASM_192.168.1.26'
    cf.HostName='192.168.1.26'
    cf.ServiceName='wxxrdb.center.wxxr.com.cn'
    
    db=OracleDB(cf)
    print db.CheckVersion()      
    print db.CheckTSUsage()
    print db.CheckStatus()
    print db.CheckASMDG()
      
            