from numbers import Number
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Resource(Base):
    __tablename__="resource"
    resource_id = Column(Integer, primary_key=True, index=True)
    resource_name  = Column(String(50), nullable = True)