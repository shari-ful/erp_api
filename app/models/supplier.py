from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Supplier(Base):
    __tablename__ = 'supplier'
    supplier_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable= False)
    currency = Column(String(10), nullable= True)
    email = Column(String(50), nullable= True)
    comment = Column(String(250), nullable= True)
    
    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)
