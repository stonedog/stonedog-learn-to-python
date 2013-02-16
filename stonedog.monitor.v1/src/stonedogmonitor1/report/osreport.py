#encodig=utf-8
'''
Created on 2013-2-16

@author: Administrator
'''

from stonedogmonitor1.window32console.console import WriteLog,WriteWaring

 
        
class OSConsoleReportDirector(object):
    def __init__(self,p_report_builder):
        self.__builder_object=p_report_builder
    
    def Report(self,p_data):
        self.__builder_object.BuildDiskPart(p_data)      

       
class OSConsoleReportBuilder(object):
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