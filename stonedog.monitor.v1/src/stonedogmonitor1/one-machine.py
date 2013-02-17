'''
Created on 2013-2-17

@author: Administrator
'''
from stonedogmonitor1.checker.dbchecker import OracleDBCheckerFactory
from stonedogmonitor1.checker.oschecker import XNixHostCheckerFactory
from stonedogmonitor1.config.initconfig import ConfigObject,ParseConfig
from stonedogmonitor1.report.dbreport import DBConsoleReportDirector,DBConsoleReportBuilder
from stonedogmonitor1.report.osreport import OSConsoleReportDirector,OSConsoleReportBuilder
import win32console
import subprocess,sys,time




if __name__=='__main__':
    hostName=sys.argv[1]
    cfile='d:\\hostimportant.conf'
    win32console.SetConsoleTitle(hostName)
    cfs=ParseConfig(cfile)
    cf=None
    for oneHost in cfs:
        if oneHost.HostName==hostName:
            cf=oneHost
    
    if cf :
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
    
    time.sleep(100)