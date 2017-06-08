import requests
import json
from get_accesstoken import access_token
from hello import openid

information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+openid+"&lang=zh_CN")

