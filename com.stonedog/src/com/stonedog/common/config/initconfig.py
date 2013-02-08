#encoding=utf-8
'''
Created on 2013-1-31

@author: Administrator
'''

import ConfigParser

class ConfigObject(object):
    def __init__(self):
        self.__dbtns=''
        self.__db_service_name=''
        
        self.__asm_tns=''
        self.__hostname=''
        
    def GetTNS(self):
        if self.__db_service_name=='':
            return self.__dbtns
        else :
            return self.__hostname+'/'+self.__db_service_name

    @property
    def TNS(self):
        return self.__dbtns
    @TNS.setter
    def TNS(self,dbtns):
        self.__dbtns=dbtns
    
    @property
    def ServiceName(self):
        return self.__db_service_name
    @ServiceName.setter
    def ServiceName(self,db_service_name):
        self.__db_service_name=db_service_name
    
    @property
    def ASMTNS(self):
        return self.__asm_tns
    @ASMTNS.setter
    def ASMTNS(self,asmtns):
        self.__asm_tns=asmtns
    
    @property
    def HostName(self):
        return self.__hostname
    @HostName.setter
    def HostName(self,hostname):
        self.__hostname=hostname
        
    

        
        
def ParseConfig(ini_file):
    '''
    根据配置文件，返回一个列表，列表成员是ConfigObject类型。
    '''
    __host_list=[]
    cf=ConfigParser.ConfigParser()
    cf.read(ini_file)
    sections=cf.sections()
    for section in sections:
        host=ConfigObject()
        host.HostName=section
        for (key,value) in cf.items(section):
            if (key.upper()=='ASM_TNS'):
                host.ASMTNS=value
            if (key.upper()=='DB_SERVICE_NAME'):
                host.ServiceName=value
            if (key.upper()=='DB_TNS'):
                host.TNS=value
        __host_list.append(host)
    
    return __host_list

if __name__=='__main__':
    l_hosts=ParseConfig("d:\\host.conf")
    for l in l_hosts:
        print l.GetTNS()
        print ('*'*5)
        print l.HostName
        print l.TNS
        print l.ASMTNS
        print l.ServiceName
        print '-'*10

'''
print len(s)
for i in s:
    print (i)
    o=cf.options(i)
    print(type(o))
    print(o)
    v=cf.items(i)
    print (type(v))
    print (v)
    print ('-'*30)
    for oo in o:
         x=cf.get(i,oo)
         print x
'''         