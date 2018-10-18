#encoding=utf-8
u'''
@created: 2018-10-18

@author: xiaolong,zeng
'''
from __future__ import division
import numpy as np
def __round__(number,ndigits=0):
    u'''
    四舍五入指定位数
    '''
    if number is None or np.isnan(number):return
    sign=-1 if number<0 else 1
    expand=np.abs(number)*10**ndigits
    
    extra=1 if np.greater_equal(expand-np.floor(expand),0.5)|np.allclose(expand-np.floor(expand),0.5) else 0
    return (np.trunc(expand)+extra)/(10**ndigits)*sign
def __rounds__(number,ndigits=0):
    u'''
    2018-05-18
    四舍六入五成双
    
    网商手续费都是按四舍六入五成双去算的
    具体规则如下：
    1. 被修约的数字小于5时，该数字舍去；
    2. 被修约的数字大于5时，则进位；
    3. 被修约的数字等于5时，要看5前面的数字，若是奇数则进位，若是偶数则将5舍掉，
    即修约后末尾数字都成为偶数；若5的后面还有不为“0”的任何数，
    则此时无论5的前面是奇数还是偶数，均应进位。
    
    举例，用上述规则对下列数据保留3位有效数字：
    9.8249=9.82, 9.82671=9.83
    9.8350=9.84, 9.8351 =9.84
    9.8250=9.82, 9.82501=9.83
    
    从统计学的角度，“四舍六入五成双”比“四舍五入”要科学，在大量运算时，
    它使舍入后的结果误差的均值趋于零，而不是像四舍五入那样逢五就入，导致结果偏向大数，
    使得误差产生积累进而产生系统误差，“四舍六入五成双”使测量结果受到舍入误差的影响降到最低。
    '''
    if number is None or np.isnan(number):return
    sign=-1 if number<0 else 1
    expand=np.abs(number)*10**ndigits
    
    extra=0
    if np.greater(expand-np.floor(expand),0.5):
        extra=1
    elif np.allclose(expand-np.floor(expand),0.5):
        if np.allclose(np.floor(expand)%2,1):
            extra=1
        pass
    
    return (np.trunc(expand)+extra)/(10**ndigits)*sign
def __ceil__(number,ndigits=0):
    u'''
    截断指定位数
    '''
    if number is None or np.isnan(number):return
    sign=-1 if number<0 else 1
    expand=np.abs(number)*10**ndigits
    return np.trunc(expand)/(10**ndigits)*sign
def __forward__(number,ndigits=0):
    u'''
    2018-05-08
    进一法指定位数
    '''
    if number is None or np.isnan(number):return
    sign=-1 if number<0 else 1
    expand=np.abs(number)*10**ndigits
    return (np.trunc(expand)+1)/(10**ndigits)*sign