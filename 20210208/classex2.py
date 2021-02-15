# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung
classex2.py : 생성자
    __init__ 생성자임
  기본생성자 : 생성자의  매개변수가 self인 생성자
"""
class Car :
    color = ""  # 초기화
    speed = 0    
    #생성자.
    def __init__(self, v1, v2):  # self :매개변수 목록의 첫번째여야 함 
        self.color = v1
        self.speed = v2        
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -= value   
       
myCar1 = Car("빨강", 10)  # v1<=빨강, v2<=10  값으로 매핑함
myCar2 = Car("노랑", 20)  # v1<=노랑, v2<=20 값으로 매칭함
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % 
                                         (myCar1.color, myCar1.speed))
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % 
                                         (myCar2.color, myCar2.speed))
