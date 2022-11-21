from numbers import Number
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Operation(Base):
    __tablename__="operation"
    operation_id = Column(Integer, primary_key=True, index=True)
    operation_name  = Column(String(50), nullable = True)