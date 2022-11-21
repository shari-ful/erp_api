from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from ..config.dbpostgres import Base

class PurchaseOrder(Base):
    __tablename__ = 'purchase_order'
    purchase_order_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable = True)
    billing_status = Column(String(50), nullable = True)
    order_no = Column(String(50), nullable = True)
    entity_type = Column(String(50), nullable = True)
    supplier_id = Column(Integer, ForeignKey("supplier.supplier_id"), nullable = True)
    currency = Column(String(100), nullable = True)
    expected_arrival_date = Column(String(50), nullable = True)
    order_created_date = Column(String(250), nullable = True)
    additional_info = Column(String(250), nullable = True)
    location_id = Column(Integer, ForeignKey("location.location_id"), nullable = True)
    
   
    tracking_location_id = Column(String(50), nullable = True)
    

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)
