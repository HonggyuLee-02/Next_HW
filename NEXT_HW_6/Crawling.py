import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup as bs
from datetime import datetime

#고려대학교 도서관
url = "https://library.korea.ac.kr/datause/collection/new/total/"
#헤더 설정
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
print(response.status_code)

soup = bs(response.text, 'html.parser')
titles = list(map(lambda x: x.text, soup.select('.item-title a')))

authors = list(map(lambda x: x.text.replace("\n",'').replace("\t",''), soup.select(".item-author")))

publishers = list(map(lambda x: x.text.replace("\n",'').replace("\t",''), soup.select('.item-pub')))

wb = Workbook()
ws = wb.active

ws.append(["제목","저자","출판사"])

for i, j, k in zip(titles,authors,publishers):
    ws.append([i,j,k])

today = datetime.now().strftime('%Y%m%d')
filename = f'고려대학교 도서관_{today}.xlsx'
wb.save(filename)
