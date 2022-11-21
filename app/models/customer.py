from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable = True)
    first_name = Column(String(50), nullable = True)
    last_name = Column(String(50), nullable = True)
    company = Column(String(150), nullable = True)
    email = Column(String(100), nullable = True)
    phone = Column(String(50), nullable = True)
    comment = Column(String(250), nullable = True)
    currency = Column(String(50), nullable = True)
    default_billing_id = Column(String(50), nullable = True)
    default_shipping_id = Column(String(50), nullable = True)

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)
