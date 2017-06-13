import requests
import json

payload = {'grant_type':'client_credential','appid':'wxdbf87277a6a9e2c3','secret':'b98898bcfe966fc2c50acaf8d6a87fc3'}

token = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxdbf87277a6a9e2c3"+"&secret=b98898bcfe966fc2c50acaf8d6a87fc3")

if 'access_token' in token.json():
    access_token = token.json()['access_token']
else:
    access_token = 'XXXXX'