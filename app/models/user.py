from sqlalchemy import Column, Integer, String, DateTime
from ..config.dbpostgres import Base

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) 