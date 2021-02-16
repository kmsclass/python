# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:16:28 2021

@author: myung

exam1.py : 
"""
import numpy as np
print("0부터 9까지 정수10개의 요소를 0으로 채운 배열 생성")
arr = np.zeros(10,dtype=int)
print(arr)
print("3행 5열의 요소를 1으로 채운 배열 생성")
arr = np.ones((3,5))
print(arr)
print("0~20 까지의 수를 2씩 증가시킨 값을 배열 생성")
arr = np.arange(0,21,2)
print(arr)
print("0 과 1 사이의 일정한 간격의  5개의 값을 가진 배열 생성")
arr = np.linspace(0,1,5)
print(arr)

print("3행 5열의 값을 3.14로 채운 배열 생성 ")
arr = np.full((3,5),3.14)
print(arr)

