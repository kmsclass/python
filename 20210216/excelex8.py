# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:22:53 2021

@author: myung
excelex8.py : 폴더에 속한  excel 파일들을 모두 읽어서  하나의 excel 파일로 생성
"""
import pandas as pd
import glob  #경로명 표현시 사용되는 모듈
import os    #시스템 관련된 모듈
inpath="C:/kms/20200914/python/workspace/excel/"
outfile="sales_all.xlsx"
#inpath : 조회되는 폴더
#*.xls* : inpath 폴더 내부의 파일 중 xls, xlsx 확장자를 가진 파일 전부
excels = glob.glob(os.path.join(inpath,"*.xls*"))
print(type(excels)) #리스트 excel 파일의 목록 
rows = [] 
for excel in excels :
    print(excel) #조회된 파일의 이름
    #excel 파일 읽기. 
    dfs = pd.read_excel(excel,sheet_name=None,index_col=None)
    for sheet_name,df in dfs.items() :
        rows.append(df)
        
df_concat = pd.concat(rows,sort=False,axis=0,ignore_index=True)
writer = pd.ExcelWriter(outfile)
df_concat.to_excel(writer,sheet_name="all_data_all_worksheet",index=False)
writer.save()