from bs4 import BeautifulSoup
import json
import requests

data = {}
data['stuid'] = '140410108'
data['pwd'] = '2010wanmei'

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}

res = requests.post('http://222.194.15.1:7777/pls/wwwbks/bks_login2.login',data, headers = headers)

soup = BeautifulSoup(res.text,"html.parser")

if soup.title:
    print('TRUE')

