import requests
import json
from get_accesstoken import access_token 

data = {
           "touser":"oqK-bxCCAxRaEHslFrJ7_UGQ8JNM",
           "template_id":"66-Ti5J6XyTzMXbVHPH-cr2NZ_xeNIHNK4FnmCJTl9Q",
           "url":"http://weixin.qq.com/download",  
           "data":{
                   "first": {
                       "value":"恭喜你购买成功！",
                       "color":"#173177"
                   },
                   "keyword1":{
                       "value":"巧克力",
                       "color":"#173177"
                   },
                   "keyword2": {
                       "value":"39.8元",
                       "color":"#173177"
                   },
                   "keyword3": {
                       "value":"2014年9月22日",
                       "color":"#173177"
                   },
                   "remark":{
                       "value":"欢迎再次购买！",
                       "color":"#173177"
                   }
           }
       }


message = requests.post("https://api.weixin.qq.com/cgi-bin/message/template/send?access_token="+access_token,data = json.dumps(data))