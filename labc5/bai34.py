# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:49:09 2024

@author: Admin
"""

n = int(input("Nhập một số nguyên dương: "))
if n <= 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    s = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s = False
            break
    if s:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
