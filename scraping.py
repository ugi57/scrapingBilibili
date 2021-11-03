import requests
from bs4 import BeautifulSoup
import csv

url='https://www.bilibili.com/v/popular/rank/all'

html=requests.get(url).content

soup=BeautifulSoup(html,'html.parser')

items=soup.find_all('li',{'class':'rank-item'})

fileName='bilibiliTop100.csv'
with open(fileName,'w',newline='',encoding='utf-8-sig') as f:
	write=csv.writer(f)
	write.writerow(['rank','title','score','play'])
	for i in items:
		title=i.find('a',{'class':'title'}).text
		score=i.find('div',{'class':'pts'}).find('div').text
		rank=i.find('div',{'class':'num'}).text
		play=i.find('span',{'class':'data-box'}).text
		data=[rank,title,score,play]
		write.writerow(data)
