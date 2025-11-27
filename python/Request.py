import requests
url='https://www.weather.com.cn'
r=requests.get(url)
r.encoding='utf-8'
print(r.text)