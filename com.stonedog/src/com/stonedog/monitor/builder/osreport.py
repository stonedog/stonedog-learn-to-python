#encoding=utf-8
'''
Created on 2013-1-27

@author: Administrator
'''

from basereport import DirectorObject,BuilderObject 
from com.stonedog.study.win32console.win32test import WriteLog,WriteWaring
class OSReportDirector(DirectorObject):
    '''
    单纯的功能类，不能有成员变量。
    '''
    def __init__(self,p_report_builder):
        self.__builder_object=p_report_builder
    
    def Report(self,p_data):
        self.__builder_object.BuildDiskUsagePart(p_data)
        self.__builder_object.BuildOSInfoPart(p_data)
        
class OSConsoleReportDirector(DirectorObject):
    def __init__(self,p_report_builder):
        self.__builder_object=p_report_builder
    
    def Report(self,p_data):
        self.__builder_object.BuildDiskPart(p_data)      

class OSTextReportBulider(BuilderObject):
    def __init__(self):
        pass
    
    def BuildDiskUsagePart(self,p_data):
        pass
    
    def BuildOSInfoPart(self,p_data):
        pass        
class OSConsoleReportBuilder(BuilderObject):
    def __init__(self):
        pass
    def BuildDiskPart(self,p_data):
        for disk in p_data:
            disk=disk.replace('\n','').replace('\r','')
#            WriteLog(disk)
            #disk=disk.replace('\n','')
            if len(disk)>1:
                up=disk.split()[4].replace('%','')
                if up.isdigit() and int(up)>70:
                    WriteWaring(disk)
                else :
                    WriteLog(disk)
        