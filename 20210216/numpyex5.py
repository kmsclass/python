# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:23:13 2021

@author: myung

numpyex5.py : 배열 사본 생성 , 재구조화 예제
"""

import numpy as np
#0~9까지의 임의의 수 10개 가진 배열 생성
x = np.random.randint(10, size = 10)
x_sub = x[:2] #0,1 인덱스를 가진 부분 배열
print(x)
print(x_sub)
x_sub[0] = 20 #부분배열을 변경시 원본배열도 변경됨 
print(x)
print(x_sub)

#배열 복사
x_cop = x.copy() #x 배열 복사.
x_cop[0]=100
print(x)
print(x_cop)

#배열의 재편성 : 재편성되는 배열의 요소의 수가 원본의 배열의 수와 같아야 한다.
x2 = x.reshape(5,2) #1차원 배열 => 2차원배열로 재편성함.
print(x2)

#0부터 99까지의 임의의 수를 9개 가진 배열 a 생성.
# a 배열을 3행3열로 재편성한 배열 b 생성하기
#재편성시 요소의 갯수가 맞아야 한다.
a = np.random.randint(100,size=9)
b = a.reshape(3,3)
print(a)
print(b)

