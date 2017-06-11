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

    def __init__(self,openid=None, stuid=None):
        self.openid = openid
        self.stuid = stuid


    def __repr__(self):
        return '<id %r name %r>' % (self.openid,self.stuid)
