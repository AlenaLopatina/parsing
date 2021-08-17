from lxml import html
import requests
from pprint import pprint

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
response = requests.get('https://lenta.ru/', headers=header)
dom = html.fromstring(response.text)
news = dom.xpath("//div[@class='item']")
news_list = []
for new_list in news:
    news_data= {}
    name = new_list.xpath("//div[@class='item']/a/text()")
    link = new_list.xpath("//div[@class='item']/a/@href")
    datatime = new_list.xpath("//div[@class='item']/a[@href]/time//text()")
    news_data['name'] = name
    news_data['link'] = link
    news_data['datatime'] = datatime
    news_data['sourse'] = 'lenta.ru'
    news_list.append(news_data)
pprint(news_list)







