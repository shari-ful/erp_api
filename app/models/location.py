from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Location(Base):
    __tablename__ = 'location'
    location_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable= True)
    legal_name = Column(String(100), nullable= True)
    address_id = Column(Integer, ForeignKey('customer_address.address_id'), nullable= True)
    is_primary = Column(Boolean, nullable= True)
    sales_allowed = Column(Boolean, nullable= True) 
    manufacturing_allowed = Column(Boolean, nullable= True)
    purchase_allowed = Column(Boolean, nullable= True)

    created_at = Column(DateTime, nullable= True)
    updated_at = Column(DateTime, nullable= True)