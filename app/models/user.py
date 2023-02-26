from pydantic import BaseModel
from typing import Optional 
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import text
from app.database import Base, SessionLocal

class UserBase(Base):
    _tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(255))

    @classmethod
    def find_by_email(cls, email):
        return SessionLocal().query(cls).filter(cls.email == email).first()
