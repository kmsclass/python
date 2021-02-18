# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:43:34 2021

@author: myung

drinkdataex2.py : 대륙별 데이터를 분석하여 파이 그래프로 출력
"""
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)
print(drinks.info())
# null의 값을 가진 건수=> 결측 데이터.
print(drinks.isnull().sum())
print(drinks.dtypes)

#fillna : 결측데이터를 "OT" 값으로 치환. 결측데이터 제거.
drinks['continent'] = drinks['continent'].fillna('OT')
#value_counts() : 값별로 건수 
labels= drinks['continent'].value_counts().index.tolist() #대륙코드 
fracs1= drinks['continent'].value_counts().values.tolist() #대륙별 등록된 갯수
explode = (0.1, 0, 0, 0, 0, 0)
print(drinks['continent'].value_counts())
print(fracs1)

plt.pie(fracs1, explode=explode, 
        labels=labels, autopct='%.1f%%', shadow=True)
plt.title('null data to \'OT\'')
plt.show()
