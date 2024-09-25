# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:20:00 2024

@author: Admin
"""
a = int(input("Nhập cạnh thứ nhất: "))
b = int(input("Nhập cạnh thứ hai: "))
c = int(input("Nhập cạnh thứ ba: "))
if a + b > c and a + c > b and b + c > a:
  print("Ba cạnh này lập thành một tam giác.")
  if a == b == c:
    print("Đây là tam giác đều.")
  elif a == b or a == c or b == c:
     if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
       print("Đây là tam giác vuông cân.")
     else:
       print("Đây là tam giác cân.")
  elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Đây là tam giác vuông.")
  else:
    print("Đây là tam giác thường.")
else:
  print("Ba cạnh này không lập thành một tam giác.")
