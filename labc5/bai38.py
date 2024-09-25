# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:21:56 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 1
if n>0 and n%2 != 0:
  for i in range(1,n+1):
     s *= i
  print('s =',s)   
else:
 print('Không hợp lệ')        