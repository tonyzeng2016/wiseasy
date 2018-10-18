#encoding=utf-8
u'''
@created: 2018-10-18

@author: xiaolong,zeng
'''
from __future__ import division
import os
import pandas as pd
import datetime

current_home= os.path.dirname(os.path.abspath(__file__))

def __date__(dateStr):
    if pd.isnull(dateStr) or dateStr is None:return
    try:
        dateStr=unicode(dateStr)
        dateStr=dateStr.encode('utf-8')
        
        dte=datetime.datetime.strptime(dateStr.strip(),'%Y-%m-%d')
        return dte.strftime('%Y-%m-%d')
    except:
        return None
def __vchar__(mcode):
    if pd.isnull(mcode) or mcode is None:return
    
    mcode=unicode(mcode)
    mcodeStr=mcode.encode('utf-8')

    return mcodeStr.strip()
def __webchat_direct_rate_zero_merchantNo__():
    u'''
    2018-08-21
    '''
    base=pd.read_excel(os.path.join(current_home,u'智慧餐饮0费率商户白名单.xlsx'),sheetname=u'商户列表')
    base[u'merchant_no']=base[u'商户号'].apply(__vchar__)
    base[u'in_date']=base[u'生效时间']
    ret=base.ix[:,[u'merchant_no',u'in_date']].copy()
    del base
    ret.sort_values(u'in_date',ascending=True,inplace=True)
    ret.drop_duplicates(u'merchant_no',keep='last',inplace=True)
    return ret
def __blue_sea_zero_merchantNo__():
    u'''
    2018-07-30
    '''
    base=pd.read_excel(os.path.join(current_home,u'蓝海活动0费率商户白名单.xlsx'),sheetname=u'商户明细')
    base[u'merchant_no']=base[u'商户号'].apply(__vchar__)
    base[u'in_date']=base[u'生效日期']
    ret=base.ix[:,[u'merchant_no',u'in_date']].copy()
    del base
    ret.sort_values(u'in_date',ascending=True,inplace=True)
    ret.drop_duplicates(u'merchant_no',keep='last',inplace=True)
    return ret
def __webchat_direct_rate_zero_mcodes__():
    u'''
    2018-08-21
    '''
    base=pd.read_excel(os.path.join(current_home,u'智慧餐饮0费率商户白名单.xlsx'),sheetname=u'开通门店明细')
    base[u'MCODE']=base[u'MCODE'].apply(__vchar__)
    #base[u'MCODE']=base[u'MCODE'].astype(str)
    
    return base[u'MCODE'].dropna().unique()
def __JF04A_rate_zero_mcodes__():
    u'''
    2018-07-30
    '''
    base=pd.read_excel(os.path.join(current_home,u'蓝海活动0费率商户白名单.xlsx'),sheetname=u'门店明细')
    base[u'MCODE']=base[u'mcode'].apply(__vchar__)
    
    return base[u'MCODE'].dropna().unique()
def __JF11_terminal_no__():
    u'''
    2018-08-21
    '''
    base=pd.read_excel(os.path.join(current_home,'汇通达华势商户统计.xlsx'),sheet_name='Sheet1')
    base[u'终端号']=base[u'终端号'].apply(__vchar__)
    
    return base[u'终端号'].dropna().unique()