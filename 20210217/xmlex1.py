'''
Created on 2020. 8. 26.
@author: GOODEE
0826/xmlex1.pyml 파일을 읽어 분석하기
'''
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
if not os.path.exists("forcast.xml") :
    req.urlretrieve(url,"forcast.xml")
    
xml = open("forcast.xml","r",encoding="utf-8").read()

info = {}
soup = BeautifulSoup (xml, "html.parser")
for location in soup.find_all("location") :
    name = location.find("city").string
    weather = location.find("wf").string
    if not (weather in info) :
        info[weather] = []
    info[weather].append(name)

for weather in info.keys() :
    print("+",weather)
    for name in info[weather] :
        print(" |- ",name)
