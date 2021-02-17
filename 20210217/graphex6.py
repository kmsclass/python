# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:52:47 2021

@author: myung

graphex6.py : : 격자 모양 그리기
"""

import numpy as np
import matplotlib.pyplot as plt

xvalue = np.linspace(0,10,11) # 0~ 10까지 균등하게 11개의 숫자를 저장 
yvalue = np.linspace(0,10,11)
#np.meshgrid : 2차형태로 저장 
x,y = np.meshgrid(xvalue,yvalue)
print(x)
print(y)
plt.figure()
#점으로 그래프 작성
plt.scatter(x,y,s=100,c="b")
plt.xlim(0,10) #x축 좌표값
plt.ylim(0,10) #y축 좌표값
plt.show()
