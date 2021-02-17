# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:31:59 2021

@author: myung

test1.py : sales_2015.xlsx 파일의 1월  Customer Name 별 Sale Amount을
           막대 그래프로 출력하기
"""

import pandas as pd
import matplotlib.pyplot as plt

infile="../excel/sales_2015.xlsx"
df = pd.read_excel(infile,"january_2015",index_col=None)
df_value = df.loc[:,["Customer Name","Sale Amount"]]

plt.style.use("ggplot")
customers = list(df_value["Customer Name"]) #x축 이름부분
print(customers)
customers_index = range(len(customers))
amounts = list(df_value["Sale Amount"]) #막대그래프의 값

#막대 그래프 출력
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#막대그래프 설정
ax1.bar(customers_index,amounts,align="center", color="darkblue")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
#x축의 이름 설정
plt.xticks(customers_index,customers,rotation=0,fontsize="small")
plt.xlabel("Coutomer")
plt.ylabel("Amount") 
plt.title("Sales Amount")
plt.savefig("sales_amount1.png", dpi=400, bbox_inches="tight")
plt.show() 