# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:30:08 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
s = 0
for i in range(1,n+1):
     s += 1/(2*i)
print('s =',s)   