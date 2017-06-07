import requests
import json
from get_accesstoken import access_token

openid = "oqK-bxCCAxRaEHslFrJ7_UGQ8JNM"

information = requests.get("https://api.weixin.qq.com/cgi-bin/user/info?access_token="+access_token+"&openid="+openid+"&lang=zh_CN")

