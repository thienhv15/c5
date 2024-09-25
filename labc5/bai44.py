# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:52:08 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 0
for i in range(n+1):
   s +=  ((2*i)+1) / ((2*i)+2)
print('s =',s)   