import requests

data = {    {
    "button":[
           {    
                "type":"click",
                        "name":"今日歌曲",
                                "key":"V1001_TODAY_MUSIC" 
                                    },
                                        { 
                                                "name":"菜单",
                                                        "sub_button":[
                                                                {   
                                                                            "type":"view",
                                                                                        "name":"搜索",
                                                                                                    "url":"http://www.heleasy.com/"
                                                                                                            },
                                                                                                                    {
                                                                                                                                "type":"view",
                                                                                                                                            "name":"视频",
                                                                                                                                                        "url":"http://www.heleasy.com/"
                                                                                                                                                                },
                                                                                                                                                                        {
                                                                                                                                                                                    "type":"click",
                                                                                                                                                                                                "name":"赞一下我们",
                                                                                                                                                                                                            "key":"V1001_GOOD"
                                                                                                                                                                                                                    }]
                                                                                                                                                                                                                            }],
                                                                                                                                                                                                                                   "matchrule":{
                                                                                                                                                                                                                                            "group_id":"2",
                                                                                                                                                                                                                                                     "sex":"1",
                                                                                                                                                                                                                                                              "country":"中国",
                                                                                                                                                                                                                                                                       "province":"广东",
                                                                                                                                                                                                                                                                                "city":"广州",
                                                                                                                                                                                                                                                                                         "client_platform_type":"2"
                                                                                                                                                                                                                                                                                                  }
                                                                                                                                                                                                                                                                                                         }}

                                                                                                                                                                                                         data = json.dumps(data)
                                                                                                                                                                                                         r = request.post('')
