# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive
import web
import random

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                STATE = random.randint(1,100)
                content = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxdbf87277a6a9e2c3&redirect_uri=http%3a%2f%2flinkeyboard.site%3a5000&response_type=code&scope=snsapi_base&state="+str(STATE)+"#wechat_redirect"
                print("content:",content)
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment
