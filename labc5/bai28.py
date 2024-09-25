# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:29:53 2024

@author: Admin
"""

n = int(input('Nhập vào n: '))
while (0>=n):
    n = int(input('Nhập vào n: '))
else:
    new = [i for i in range(1,n+1) if n%i==0]
print(new)