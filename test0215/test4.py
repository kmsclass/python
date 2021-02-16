# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:08:06 2021

@author: myung

test4.py : sales_2013.xlsx 파일의  모든 sheet의 
           열이  "Customer Name", "Sale Amount" 컬럼만 
         sales_2013_allamt.xlsx 파일로 저장하기    
"""
import pandas as pd
infile="sales_2013.xlsx"
outfile = "sales_2013_allamt.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None,index_col=None)
for worksheet_name,data in df.items() :
    #data : 한개의 sheet의 데이터 저장
    #worksheet_name : sheet의 이름
    print("===",worksheet_name,"===")    
    data_value = data.loc[:,["Customer Name","Sale Amount"]]
    #writer : excel 파일
    # to_excel () : sheet를 추가.
    data_value.to_excel(writer,sheet_name=worksheet_name,index=False)
writer.save() 
