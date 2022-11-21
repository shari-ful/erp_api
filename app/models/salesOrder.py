from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class SalesOrder(Base):
    __tablename__ = 'sales_order'
    sales_order_id = Column(Integer, primary_key=True, index=True)

    order_no = Column(String(50), nullable = True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable = True)
    tracking_number = Column(String(50), nullable = True)
    tracking_number_url = Column(String(150), nullable = True)
    order_created_date = Column(String(50), nullable = True)
    delivery_date = Column(String(50), nullable = True)
    currency = Column(String(20), nullable = True)
    location_id = Column(String(50), nullable = True)
    status = Column(String(50), nullable = True)
    additional_info = Column(String(200), nullable = True)
    
    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)


class Attributes(Base):
    __tablename__ = 'attributes'
    attributes_id = Column(Integer, primary_key=True, index=True)
    key = Column(String(50), nullable= False)
    value = Column(String(50), nullable= False)
