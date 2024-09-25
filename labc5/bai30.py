# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:09:47 2024

@author: Admin
"""

thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if 1 <= thang <= 12:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        nam_nhuan = True
    else:
        nam_nhuan = False
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        so_ngay = 31
    elif thang in [4, 6, 9, 11]:
        so_ngay = 30
    elif thang == 2:
        if nam_nhuan:
            so_ngay = 29
        else:
            so_ngay = 28
    print(f"Tháng đó có {so_ngay} ngày.")
else:
    print("Tháng không hợp lệ")
