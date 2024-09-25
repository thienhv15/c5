# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 13:46:48 2024

@author: Admin
"""

N = int(input("Nhập số nguyên dương N: "))
tong = 0
for i in str(N):
    tong += int(i)
print("Tổng các chữ số của N là:", tong)
