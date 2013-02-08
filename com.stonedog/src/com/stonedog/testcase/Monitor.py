#encoding=utf-8

from com.stonedog.common.config.CSVConfig import CSVConfig 
from com.stonedog.common.db.oracledb import OracleDB,DBState
from com.stonedog.monitor.command.dbcommands import DBTSCommand,DBAASCommand
from com.stonedog.monitor.Factory.DBFactory import  DBFactory
from com.stonedog.common.config.initconfig import ConfigObject,ParseConfig
cl=ParseConfig('d:\\host.conf')
l_dbfactory=DBFactory()
l_db=l_dbfactory.CreateSession('sys','H2oisWater',"192.168.1.14:1521/wxxrdb.center.wxxr.com.cn")
l_ts_command=l_dbfactory.CreateTSCommand(l_db)
l_aas_command=l_dbfactory.CreateAASCommand(l_db)
l_rep_builder=l_dbfactory.CreateTxtReportBuilder()
l_rep_director=l_dbfactory.CreateReportDirector(l_rep_builder)

l_dbstate=DBState()
l_dbstate.TSUsage=l_ts_command.Execute()
l_dbstate.AAS=l_aas_command.Execute()


l_asmdb=l_dbfactory.CreateSession('sys','H2oisWater','ASM_192.168.1.26')
l_asmdg_command=l_dbfactory.CreateASMDGCommand(l_asmdb)
l_dbstate.ASMDG=l_asmdg_command.Execute()

l_report=l_rep_director.Report(l_dbstate)

