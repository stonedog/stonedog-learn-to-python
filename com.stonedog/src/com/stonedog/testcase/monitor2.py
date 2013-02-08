#encoding=utf-8
'''
Created on 2013-2-1

@author: Administrator
'''
from com.stonedog.monitor2.dbchecker import OracleDBCheckerFactory
from com.stonedog.monitor2.oschecker import XNixHostCheckerFactory
from com.stonedog.common.config.initconfig import ConfigObject,ParseConfig
from com.stonedog.monitor.builder.dbreport import DBConsoleReportDirector,DBTxtReportBuilder,DBConsoleReportBuilder
from com.stonedog.monitor.builder.osreport import OSConsoleReportDirector,OSConsoleReportBuilder
if __name__=='__main__':
    print('Select Mode : 1:important province')
    print ('2:normal mode')
    choice=raw_input()
    if choice=='1':
        cfile='d:\\hostimportant.conf'
    else :
        cfile='d:\\host.conf'
    cfs=ParseConfig(cfile)
    
    
    #dbcheckers=[OracleDBCheckerFactory.GetDBChecker(cf) for cf in cfs]
    for cf in cfs:
        dbchecker=OracleDBCheckerFactory.GetDBChecker(cf)
        oschecker=XNixHostCheckerFactory.GetHostChecker(cf)
        rpt_dbbuilder=DBConsoleReportBuilder()
        rpt_dbdirector=DBConsoleReportDirector(rpt_dbbuilder)
        
        rpt_osbuilder=OSConsoleReportBuilder()
        rpt_osdirector=OSConsoleReportDirector(rpt_osbuilder)
    
        ds=dbchecker.Check()
        os=oschecker.Check()
        rpt_dbdirector.Report(ds)
        rpt_osdirector.Report(os) 
        print('Press any key to continue....')
        ch=raw_input()
    
    
    