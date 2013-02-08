'''
Created on 2013-1-31

@author: Administrator
'''
#encoding=utf-8
TS_SQL='''
with a as (select tablespace_name,trunc(sum(bytes_free+bytes_used)/1024/1024) sum_m,trunc(sum(bytes_free)/1024/1024) free_m 
from v$temp_space_header group by tablespace_name
union
select a.tablespace_name,trunc(a.total/1024/1024) sum_m,trunc((a.total-b.use)/1024/1024) free_m 
from (SELECT tablespace_name,SUM(bytes) total 
      FROM dba_data_files 
      WHERE tablespace_name =(select upper(value) from v$parameter where name='undo_tablespace') group by tablespace_name) a,
     (SELECT (NVL(SUM(bytes), 0)) use FROM 
       dba_undo_extents 
       WHERE tablespace_name = (select value from v$parameter where name='undo_tablespace') AND status IN ('ACTIVE', 'UNEXPIRED')) b
union
select a.TABLESPACE_NAME,a.total sum_m,b.free free_m from (select TABLESPACE_NAME, trunc(sum(bytes) / (1024 * 1024)) total 
from sys.dba_data_files dbf 
where dbf.TABLESPACE_NAME not in (select value from gv$parameter where name = 'undo_tablespace') group by TABLESPACE_NAME ) a,
(select TABLESPACE_NAME, trunc(sum(bytes) / (1024 * 1024)) free from sys.dba_free_space group by tablespace_name) b 
where a.TABLESPACE_NAME = b.TABLESPACE_NAME
)
select tablespace_name,sum_m,free_m,trunc((sum_m-free_m)*100/sum_m) used_p
from a
'''    

ASM_DG_SQL='''
select name,trunc(total_mb/1024) tg,trunc(free_mb/1024) fg,trunc((total_mb-free_mb)*100/total_mb) up from v$asm_diskgroup    
'''
VERSION_SQL='''
select banner from v$version
'''