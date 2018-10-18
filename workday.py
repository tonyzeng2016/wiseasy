#encoding=utf-8
u'''
@created: 2018-10-18

@author: xiaolong,zeng
'''
from __future__ import division
import numpy as np
import datetime
def __wiseasy_workday_diff__(dateTime,diff=1):
    u'''
    2018-06-20
    某日的前num工作日:
    /wiseasy/workday/diff/?day=xxxx&num=xxxx
    
    day必须,不包括改日
    num可选,默认为1
    
    返回结果:{flag:xx,workday:xxx}
    flag
    0--正确
    2--格式错误
    1--参数不存在
    3--找不到工作日错误
    '''
    counter=0
        
    diff=1 if diff==0 else diff
    flag=-1 if diff<0 else 1
    
    for i in range(1,np.abs(diff)+30):
        currentDte=dateTime+datetime.timedelta(days=i*flag)
        isworkday=__wiseasy_workday__(currentDte) if currentDte.year==2018 else False
        if isworkday:counter+=1
        #print i,currentDte,isworkday,counter
        if counter>=np.abs(diff):return currentDte
    return
def __wiseasy_workday__(dateTime):
    offdays={u'元旦':{u'begin':u'2017-12-30',u'end':u'2018-01-01'},
            u'春节':{u'begin':u'2018-02-15',u'end':u'2018-02-21'},
            u'清明节':{u'begin':u'2018-04-05',u'end':u'2018-04-07'},
            u'劳动节':{u'begin':u'2018-04-29',u'end':u'2018-05-01'},
            u'端午节':{u'begin':u'2018-06-16',u'end':u'2018-06-18'},
            u'中秋节':{u'begin':u'2018-09-22',u'end':u'2018-09-24'},
            u'国庆节':{u'begin':u'2018-10-01',u'end':u'2018-10-07'}
            }
    ondays={u'春节':[u'2018-02-11',u'2018-02-24'],
            u'清明节':[u'2018-04-08'],
            u'劳动节':[u'2018-04-28'],
            u'国庆节':[u'2018-09-29',u'2018-09-30']
            }
    if dateTime.year!=2018:return False
    (_,_,day)=dateTime.isocalendar()
    
    for _,v in offdays.iteritems():
        begin=datetime.datetime.strptime(v['begin'],'%Y-%m-%d')
        end=datetime.datetime.strptime(v['end'],'%Y-%m-%d')
        if begin<=dateTime<=end:
            return False
    for _,v in ondays.iteritems():
        days=[datetime.datetime.strptime(item,'%Y-%m-%d') for item in v]
        if dateTime in days:
            return True
    if 6<=day<=7:
        return False
    return True