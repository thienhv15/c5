# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:50:55 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 0
for i in range(1,n+1):
   s +=  i / (i+1)
print('s =',s)