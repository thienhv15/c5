# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:14:13 2024

@author: Admin
"""

x = float(input("Nhập giá trị của x: "))
n = int(input("Nhập giá trị của n: "))
S = 0
for i in range(1, n + 1):
    x1 = x ** i
    h = 0
    for j in range(1, i + 1):
        h += j
    S += x1 / h
print(S)
