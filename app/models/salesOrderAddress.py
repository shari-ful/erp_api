from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from ..config.dbpostgres import Base

class SalesOrderAddress(Base):
    __tablename__ = 'sales_order_address'
    address_id = Column(Integer, primary_key=True, index=True)
    sales_order_id = Column(Integer, ForeignKey("sales_order.sales_order_id"), nullable = True)
    entity_type = Column(String(50), nullable = True)
    first_name = Column(String(50), nullable = True)
    last_name = Column(String(50), nullable = True)
    company = Column(String(100), nullable = True)
    phone = Column(String(50), nullable = True)
    line_1 = Column(String(250), nullable = True)
    line_2 = Column(String(250), nullable = True)
    city = Column(String(50), nullable = True)   
    state = Column(String(50), nullable = True)
    zip = Column(String(50), nullable = True)
    country = Column(String(250), nullable = True)
    
    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)

