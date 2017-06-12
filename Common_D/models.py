from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    openid = Column(String(50), primary_key=True)
    name = Column(String(50))
    phone = Column(String(50))
    stuid = Column(String(100))
    wechatid = Column(String(100))
    sex = Column(Integer)

    def __init__(self,openid=None, name=None, phone=None, stuid=None, wechatid=None, sex=1):
        self.openid = openid
        self.name = name
        self.phone = phone
        self.stuid = stuid
        self.wechatid = wechatid
        self.sex = sex

    def __repr__(self):
        return '<id %r name %r>' % (self.openid,self.name)

class Stu(Base):
    __tablename__ = 'stu'
    openid = Column(String(50), primary_key=True)
    stuid = Column(String(100))
    nickname = Column(String(100))
    headimgurl = Column(String(200))


    def __init__(self,openid=None, stuid=None, nickname= None, headimgurl=None):
        self.openid = openid
        self.stuid = stuid
        self.nickname = nickname
        self.headimgurl = headimgurl

    def __repr__(self):
        return '<id %r name %r>' % (self.openid,self.stuid)



class Order(Base):
    __tablename__ = 'taxiorder'
    id = Column(Integer, primary_key=True, autoincrement = True)
    openid = Column(String(50))
    fromwhere = Column(String(200))
    towhere = Column(String(200))
    whenis = Column(String(200))
    countis = Column(Integer)

    def __init__(self,openid=None,fromwhere="哈尔滨工业大学（威海）", towhere = None, whenis = None, countis = 0):
        self.openid = openid
        self.fromwhere = fromwhere
        self.towhere = towhere
        self.whenis = whenis
        self.countis = countis
        


    def __repr__(self):
        return '<id %r towhere %r count %r>' % (self.openid,self.towhere,self.countis)
