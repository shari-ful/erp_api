from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from ..config.dbpostgres import Base

class TaxRate(Base):
    __tablename__='tax_rate'
    tax_rate_id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(100), nullable= True)
    rate = Column(Float, nullable= True)
    is_default_sales = Column(Boolean, nullable= True)
    is_default_purchases = Column(Boolean, nullable = True)
    display_name = Column(String(100), nullable= True)

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)