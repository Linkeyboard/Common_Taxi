import requests
import json
from get_accesstoken import access_token 

senddata = {
    "touser":'oqK-bxCCAxRaEHslFrJ7_UGQ8JNM',
    "template_id":"9P24eASJx9m5yNSXbA6wo4qf6HOaWhJBt35pN1XZh1M",
    "url":"https://www.baidu.com",
    "data":{
        "first": {
            "value":"提示：加入活动成功！",
            "color":"#173177"
            },
        "keynote1":{
            "value":"asdf",
            "color":"#173177"
            },
        "keynote2": {
            "value":"aaa",
            "color":"#173177"
            },
        "keynote3": {
            "value":"aaa",
            "color":"#173177"
            },
        "keynote4": {
            "value":"aaa",
            "color":"#173177"
            },
        "keynote5": {
            "value":"aaa",
            "color":"#173177"
            },
        "remark":{
            "value":"请按时到达集合地！",
            "color":"#173177"
            }
    }
}
message = requests.post('https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+access_token,data = json.dumps(senddata))
print(message)


