# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 11:48:57 2021

@author: myung

selenuim4.py : 화면 이미지 저장하기
"""
from selenium import webdriver 
url = "http://www.naver.com/"
driver = webdriver.Chrome("C:/kms/20200914/setup/chromedriver")
driver.get(url)
#open된 브라우저의 화면을 이미지로 저장하기
driver.save_screenshot("naverhome.png") 
driver.quit()

