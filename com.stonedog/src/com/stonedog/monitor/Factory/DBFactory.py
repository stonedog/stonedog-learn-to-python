#encoding=utf-8

from com.stonedog.common.db.oracledb import OracleDB
from com.stonedog.monitor.command.dbcommands import DBTSCommand,DBAASCommand,DBASMDGCommand
from com.stonedog.monitor.builder.dbreport import DBTxtReportBuilder,DBReportDirector,DBHtmlReportBuilder

class DBFactory(object):
    def __init__(self):
        pass
    
    def CreateSession(self,username,password,tnsname):
        return OracleDB(username,password,tnsname)
    
    def CreateAASCommand(self,p_db):
        return DBAASCommand(p_db)
    
    def CreateASMDGCommand(self,p_db):
        return DBASMDGCommand(p_db)
         
    
    def CreateTSCommand(self,p_db):
        return DBTSCommand(p_db)
    
    def CreateTxtReportBuilder(self):
        return  DBTxtReportBuilder()
        
    
    def CreateHTMLReportBuilder(self):
        return DBHtmlReportBuilder()
    
    def CreateReportDirector(self,p_report_builder):
        return DBReportDirector(p_report_builder)
    


          