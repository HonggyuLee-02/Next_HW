from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from openpyxl import Workbook
from datetime import datetime

chromedriver_path = "C:\\Users\\UserK\\Desktop\\NEXT\\Session\\NEXT_Session_6\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
user_data_dir = "C:\\Users\\UserK\\Desktop\\NEXT\\HW\\NEXT_HW_6\\Userdata"
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
#고려대 도서관 접속
driver.get("https://library.korea.ac.kr/datause/collection/new/total/#")

titles =[]
authors = []
publishers = []
today = datetime.now().strftime('%Y%m%d')
wb = Workbook()
ws = wb.active
ws.append(["제목",'저자','출판사'])
for j in range(1,67):
        for i in range(1,12+1):
            title = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[{i}]/div/div[2]/div[1]/h4/a').text
            author = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[{i}]/div/div[2]/div[2]').text
            publisher = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[{i}]/div/div[2]/div[3]').text
            ws.append([title,author,publisher])
        next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/article/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/button[2]')
        next_button.click()
        
title = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[1]/h4/a').text
author = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]').text
publisher = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/article/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]').text
ws.append([title,author,publisher])
filename = f'{today}korea_univ_library.xlsx'
wb.save(filename)
time.sleep(1)
