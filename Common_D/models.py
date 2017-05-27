from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    phone = Column(String(50))
    wechat_id = Column(String(100))

    def __init__(self,id=None, name=None, phone=None, wechat_id=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.wechat_id = wechat_id



    def __repr__(self):
        return '<id %r name %r>' % (self.id,self.name)