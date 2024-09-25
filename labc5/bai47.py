# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:19:41 2024

@author: Admin
"""

a = 0
b = None
for x in range(1, 490):  
    for y in range(1, 141): 
        for z in range(1, 109): 
            if 2 * x + 7 * y + 9 * z == 979:
                c = x + y + z
                if c > a:
                    a = c 
                    b = (x, y, z)
if b:
    print("Bộ nghiệm nguyên với x, y, z > 0 và x + y + z lớn nhất:")
    print(f"x = {b[0]}, y = {b[1]}, z = {b[2]}")
    print(f"x + y + z = {a}")
else:
    print("Không có bộ nghiệm nào thỏa mãn điều kiện.")
