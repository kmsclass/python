# -*- coding: utf-8 -*-
"""
python2.py
print(출력값1,출력값2,...)
print("형식지정문자를 가진 문자열",(출력값1,출력값2,...))
print(출력값,end="") : end =마지막 문자 지정. 기본값 \n
print(format 함수 지정하기)
"""
a = int(input("값1 입력:")) #100
b = int(input("값2 입력:")) #200
result = a+b
print(a,"+",b,"=",result)
print("%d + %d = %d" % (a,b,result))
print("안"+"녕") #문자열+문자열 가능
#print(a+"+"+b+"="result) #오류발생. 문자열+숫자형 연산안됨
print("안녕하세요",end=":")
print("홍길동 입니다.")
#format 함수 사용하기
print("{0:d} {1:5d} {2:05d}".format(100,200,300))
print("{2:d} {1:5d} {0:05d}".format(100,200,300))

# * 연산자 사용하기 
print("abc"+"abc"+"abc")
print("abc","abc","abc")
print("abc"*3)
# """ 문자열 연결하여 출력하기
print("안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ...."
      + "안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....")
print("""안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....
      안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....""")
print('안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....'
      + '안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....')
print('''안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....
      안녕하세요 홍길동 입니다. 반값습니다. 어쩌구 저쩌구 ....''')






