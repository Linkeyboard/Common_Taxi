import requests
import json
from threading import Timer


payload = {'grant_type':'client_credential','appid':'wxdbf87277a6a9e2c3','secret':'b98898bcfe966fc2c50acaf8d6a87fc3'}


def get_ac():
    token = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxdbf87277a6a9e2c3"+"&secret=b98898bcfe966fc2c50acaf8d6a87fc3")
    print(token.json())
    global access_token
    access_token = token.json()['errmsg']
    t = Timer(10,get_ac)
    t.start()

get_ac()
print(access_token)
