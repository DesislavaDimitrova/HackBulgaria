from sqlalchemy import Column, Integer, String
from connection import Base


class Players(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    highscore = Column(Integer)
