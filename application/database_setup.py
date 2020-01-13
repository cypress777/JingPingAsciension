import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
DatabaseName = 'ascension_userinfo.db'

class UserInfo(Base):
  __tablename__ = 'userinfo'

  id = Column(Integer, primary_key=True)
  name = Column(String(32), nullable=False)
  password = Column(String(8))

engine = create_engine('sqlite:///{}'.format(DatabaseName))

Base.metadata.create_all(engine)
