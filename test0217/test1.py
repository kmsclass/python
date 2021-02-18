# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:22:56 2021

@author: myung

test1.py : 
   1.http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp
   의 내용을 받아서 forcast.xml 파일로 저장하기.
   2. 저장된 파일을 읽어서  
   다음 결과가 나오도록 프로그램 구현하시오
"""
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
if not os.path.exists("forcast.xml") :
    req.urlretrieve(url,"forcast.xml") #파일에 저장.
    
xml = open("forcast.xml","r",encoding="utf-8").read()

info = {} #dictionary
soup = BeautifulSoup (xml, "html.parser")
for location in soup.find_all("location") :
    name = location.find("city").string  #도시명
    weather = location.find("wf").string #흐림, 맑음
    if not (weather in info) : #새로운 날씨정보.
        info[weather] = [] # 도시 저장.
    info[weather].append(name)

for weather in info.keys() :
    print("+",weather)
    for name in info[weather] :
        print(" |- ",name)

