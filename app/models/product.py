from numbers import Number
from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Product(Base):
    __tablename__="product"
    product_id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable = True)
    uom = Column(String(50), nullable = True)
    category_name = Column(String(50), nullable = True)
    is_producible = Column(Boolean, nullable = True)
    default_supplier_id = Column(Integer, nullable = True)
    is_purchasable = Column(Boolean, nullable = True)
    type = Column(String(100), nullable = True)
    additional_info = Column(String(50), nullable = True)
    purchase_uom = Column(String(50), nullable = True)
    purchase_uom_conversion_rate = Column(Integer, nullable = True)
    batch_tracked = Column(Boolean, nullable = True)

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)
