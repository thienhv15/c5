# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:32:06 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 0
for i in range(n+1):
   s +=  1 / (2 * i + 1)
print('s =',s)   