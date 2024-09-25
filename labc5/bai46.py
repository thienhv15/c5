# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:19:16 2024

@author: Admin
"""

s = 979
for x in range(1, s // 2 + 1):  
    for y in range(1, s // 7 + 1):  
        for z in range(1, s // 9 + 1):
            if 2 * x + 7 * y + 9 * z == 979:
                print(f"x = {x}, y = {y}, z = {z}")
