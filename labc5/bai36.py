# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:16:10 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 0
if n>0:
  for i in range(1,n+1):
     s += i**2
  print('s =',s)   
else:
 print('Không hợp lệ')    