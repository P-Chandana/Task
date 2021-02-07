import unittest

import calendar
from numpy import linalg
import numpy as np

def find_day(dt):
    year, month, day = map(int, dt.split('-'))
    day_num = calendar.weekday(year, month, day)
    # return calendar.day_name[day_num][:3]
    return day_num

def solve(days):
    lst = []
    for i in range(len(days)):
        if days[i] == 0:
            lst.append(1)
        else:
            lst.append(days[i])
            
    x, ca, cb, cc, cd, ce, y = lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6]
    A = [[-2*ca, cb, 0, 0, 0],
         [ca, -2*cb, cc, 0, 0],
         [0, cb, -2*cc, cd, 0],
         [0, 0, cc, -2*cd, ce],
         [0, 0, 0, cd, -2*ce]]
    B = [-x, 0, 0, 0, -y]
    
    C = [[-2*ca, cb, 0, 0, 0],
         [ca, -2*cb, cc, 0, 0],
         [0, cb, -2*cc, cd, 0],
         [0, 0, cc, -2*cd, ce],
         [0, 0, 0, cd, -2*ce]]
         
    X = []
    for i in range(0,len(B)):
        for j in range(0,len(B)):
            C[j][i]=B[j]
            if i>0:
                C[j][i-1]=A[j][i-1]
        X.append(round(linalg.det(C)/linalg.det(A),1))
    #print(X)
    return X

def create_new_dic(dic):
    days = [0]*7
    for date in dic:
        day = find_day(date)
        days[day] += dic[date]
    #print(days)
    ansX = solve(days)
    for i in range(5):
        if (days[i+1] == 0):
            days[i+1] = 1
        days[i+1] = days[i+1]*ansX[i]
    #print(days)
    return days

# d = {'2020-01-01':4, '2020-01-02':4, '2020-01-03':6, '2020-01-04':8, '2020-01-05':2, '2020-01-06':-6, '2020-01-07':2, '2020-01-08':-2}
d = {'2020-01-01':6, '2020-01-04':12, '2020-01-05':14, '2020-01-06':2, '2020-01-02':4}

new_dic_lst = create_new_dic(d)
new_dic = {}
for i in range(len(new_dic_lst)):
    day = calendar.day_name[i][:3]
    new_dic[day] = new_dic.get(day, 0) + new_dic_lst[i]

print(new_dic)
# print(find_day('2020-01-05'))

class testdic(unittest.TestCase):
  D1=new_dic
  D2={'Mon': 2, 'Tue': 4.0, 'Wed': 6.0, 'Thu': 8.0, 'Fri': 10.0, 'Sat': 12.0, 'Sun': 14}
  def test(self):
        self.assertDictEqual(self.D1, self.D2)
