# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:02:45 2024

@author: Admin
"""

n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Hãy nhập một số nguyên dương.")
else:
    a = False
    for i in range(1, n + 1):
        if i * i == n:
            a = True
            break
    if a:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
