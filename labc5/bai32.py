# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:13:32 2024

@author: Admin
"""

km = float(input("Nhập số km đã đi: "))
gia_1km = 15000
gia_2_5km = 13500
gia_6km = 11000
tong_tien = 0
for i in range(1, int(km) + 1):
    if i == 1:
        tong_tien += gia_1km
    elif 2 <= i <= 5:
        tong_tien += gia_2_5km  
    else:
        tong_tien += gia_6km  
if i > 120:
    tong_tien *= 0.9
print(f"Tổng tiền cước taxi là: {tong_tien} VND")
