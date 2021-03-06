# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:27:04 2021

@author: myung
graphex4.py : 그래프 그리기 graphex1.py의 그래프 내용을 한글로 변경
"""
import matplotlib.pyplot as plt
#한글 처리를 위한 설정 
#한글이 가능한 폰트로 설정해야 한글이 보여짐.
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties\
            (fname="c:/Windows/Fonts/malgun.ttf").get_name()
print(font_name) #맑은 고딕            
rc('font', family=font_name) #현재 폰트 변경 설정.


plt.style.use("ggplot")
subjects = ["자바","JSP","스프링","하둡","파이"]  #막대그래프의 x좌표의 값
print(range(len(subjects)))
subjects_index = range(len(subjects)) #subjects_index : 0 ~ 4값을 저장 
print(type(subjects_index))
scores = [65,90,85,60,95] #막대그래프로 표현할 값.
#그래프 출력.
fig = plt.figure() #그래프를 그릴 수 있는 공간. 도화지.
#도화기 영역 분리. 하나의 도화지에 여러개의 그림 가능.
#1행 1열 분리 => 한개 그림. 분리안함.
# 1 : 1번째 그림.
#ax1 : 그래프가 그려지는 영역
ax1 = fig.add_subplot(1,1,1)
#ax1.bar : 막대 그래프 
#subjects_index : x좌표 내용 인덱스
#scores : 막대그래프로 표현할 데이터 값
ax1.bar(subjects_index,scores,align="center", color="darkblue")
#xaxis : x축. 위치.
#yaxis : y축. 위치.
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
# xticks : x축 
#rotation : x축에 표시되는 내용의 방향
plt.xticks(subjects_index,subjects,rotation=0,fontsize="small")
#x 축 제목
plt.xlabel("과목")
plt.ylabel("점수") #y축 제목
plt.title("과정 점수")
#메모리 저장된 이미지 파일로 생성 
plt.savefig("bar_plot.png", dpi=400, bbox_inches="tight")
plt.show() #메모리에 있는 그래프이미지를 화면 보여줌.