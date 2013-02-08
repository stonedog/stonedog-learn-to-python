#encoding=utf-8
'''
Created on 2013-1-27

@author: Administrator
'''
from basereport import DirectorObject,BuilderObject
from com.stonedog.common.db.oracledb import OracleDB
from com.stonedog.study.win32console.win32test import WriteLog,WriteWaring

class DBReportDirector(DirectorObject):
    def __init__(self,p_report_builder):
        self.__builder_object=p_report_builder
    
    def Report(self,p_data):
        self.__builder_object.BuildInfoPart(p_data)
        #self.__builder_object.BuildVersionPart(p_data)
        self.__builder_object.BuildTSPart(p_data)
        #self.__builder_object.BuildAASPart(p_data)
        self.__builder_object.BuildASMDGPart(p_data)
        
class DBConsoleReportDirector(DirectorObject):
    def __init__(self,p_report_builder):
        self.__builder_object=p_report_builder
    
    def Report(self,p_data):
        delimters=[' ','~',' ']
        for s in delimters:
            WriteLog(s*80)
        self.__builder_object.BuildInfoPart(p_data)
        #self.__builder_object.BuildVersionPart(p_data)
        self.__builder_object.BuildTSPart(p_data)
        #self.__builder_object.BuildAASPart(p_data)
        self.__builder_object.BuildASMDGPart(p_data)        
        

class DBTxtReportBuilder(BuilderObject):
    def __init__(self):
        pass
    
    def BuildInfoPart(self,p_data):
        ls=''
        ls+=p_data.HostName+':'+p_data.ServiceName+':'+p_data.TNS+':'+p_data.Status+'\n'
        return ls

    def BuildVersionPart(self,p_data):
        ls=''
        for s in p_data.Version:
            ls+=s
        
        return ls
        
    def __buildspacepart(self,p_data):
        l_s=''
        for i in p_data:
            l_s+='%20s:%10s:%10s:%10s\n' % (i[0],i[1],i[2],i[3])
        return l_s
    

        
    def BuildTSPart(self,p_data):
        l_s="表空间使用情况\n\n"
        l_s+='%20s:%10s:%10s\n' % ('表空间','总量(M)','剩余(M),使用百分比')
        l_s+='-'*30+'\n'
        l_tss=p_data.TSUsage
        
        l_s+=self.__buildspacepart(l_tss)
        
        return l_s
    
    def BuildASMDGPart(self,p_data):
        l_s="ASM DG 使用情况\n\n"
        l_s+='%20s:%10s:%10s\n' % ('DG','总量(M)','剩余(M),使用百分比')
        l_s+='-'*30+'\n'
        l_tss=p_data.ASMDG
        
        l_s+=self.__buildspacepart(l_tss)
        return l_s         
         
    
    def BuildAASPart(self,p_data):
        l_ass=p_data.AAS
        for i in l_ass:
            print ('%s = %s' %(i[0],i[1]))
            


class DBConsoleReportBuilder(BuilderObject):
    '''
目前和上面的完全一样
    '''
    
    def __init__(self):
        pass
        
    
    def BuildInfoPart(self,p_data):
        ls=p_data.HostName+':'+p_data.ServiceName+':'+p_data.TNS+':'+p_data.Status
        WriteLog(ls)
        

    def BuildVersionPart(self,p_data):
        for s in p_data.Version:
            WriteLog(s)
        
        
    def __buildspacepart(self,p_data):
        for i in p_data:
            l_s='%20s:%10s:%10s:%10s' % (i[0],i[1],i[2],i[3])
            swap=False
            if int(i[3]>80):
                WriteWaring(l_s)
            else :
                WriteLog(l_s)

        
    def BuildTSPart(self,p_data):
        l_s=["Tablespace Usage",'%20s:%10s:%10s' % ('TS','All(M)','Free(M),Used%'),'-'*30]
        for s in l_s:
            WriteLog(s)
        
        l_tss=p_data.TSUsage
        
        self.__buildspacepart(l_tss)
        

    
    def BuildASMDGPart(self,p_data):
        
        l_s=['ASM DG Usage','%20s:%10s:%10s' % ('DG','All(M)','Free(M),Used%'),'-'*30]
        for s in l_s:
            WriteLog(s)  
        
        l_tss=p_data.ASMDG
        
        self.__buildspacepart(l_tss)
        
                 
         
    
    def BuildAASPart(self,p_data):
        pass
                     

class DBHtmlReportBuilder(BuilderObject):
    def __init__(self):
        pass
    
    def BuildTSPart(self,p_data):
        pass
    
    def BuildAASPart(self,p_data):
        pass    
    