from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    opnid = Column(String(50), primary_key=True)
    name = Column(String(50))
    phone = Column(String(50))
    stuid = Column(String(100))
    wechatid = Column(String(100))

    def __init__(self,opnid=None, name=None, phone=None, stuid=None, wechatid=None):
        self.opnid = opnid
        self.name = name
        self.phone = phone
        self.stuid = stuid
        self.wechatid = wechatid


    def __repr__(self):
        return '<id %r name %r>' % (self.opnid,self.name)

class Stu(Base):
    __tablename__ = 'stu'
    opnid = Column(String(50), primary_key=True)
    stuid = Column(String(100))

    def __init__(self,opnid=None, stuid=None):
        self.opnid = opnid
        self.stuid = stuid


    def __repr__(self):
        return '<id %r name %r>' % (self.opnid,self.stuid)
