#encoding=utf-8
'''
Created on 2013-1-31

@author: Administrator
'''

class DB(object):
    def __init__(self):
        self._connection=None
        self._cursor=None
    
    def _check_space(self,sql):
        '''
                    检查空间使用情况,适用于表空间、ASM磁盘组空间
                   返回的是一个数组，每个成员是个元组（空间名、全部、可用）
       [('Product','80M','10M'),(..)...]
       '''
        l_ts=[]
        self._cursor.execute(sql)
        row=self._cursor.fetchone()
        while row:
            (ts,sum_m,free_m,up)=(row[0],row[1],row[2],row[3])
            l_one_ts=(ts,sum_m,free_m,up)
            l_ts.append(l_one_ts)
            row=self._cursor.fetchone()
      
        return l_ts