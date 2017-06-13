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



class Join(Base):
    __tablename__ = 'joining'
    joinid = Column(Integer, primary_key=True, autoincrement = True)
    openid = Column(String(50))
    followid = Column(Integer)

    def __init__(self,openid=None, followid = 0):
        self.openid = openid
        self.followid = followid
        


    def __repr__(self):
        return '<openid %r follow %r>' % (self.openid,self.followid)





class GOHOME(Base):
    __tablename__ = 'gohome'
    homeid = Column(Integer, primary_key=True, autoincrement = True)
    openid = Column(String(100))
    fromhome = Column(String(100))
    tohome = Column(String(100))
    typehome = Column(String(100))
    whenhome = Column(String(100))
    counthome = Column(String(100))

    def __init__(self,openid=None, fromhome = None, tohome = None,typehome = None, whenhome = None, counthome = 0):
        self.openid = openid
        self.fromhome = fromhome
        self.tohome = tohome
        self.typehome = typehome
        self.whenhome = whenhome
        

    def __repr__(self):
        return '<openid %r fromhome %r tohome %r>' % (self.openid,self.fromhome,self.tohome)