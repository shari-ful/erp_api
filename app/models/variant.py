from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..config.dbpostgres import Base
import datetime

class Variant(Base):
    __tablename__ = 'variant'
    variant_id = Column(Integer, primary_key=True, index=True)

    sku = Column(String, nullable= True)
    sales_price = Column(Integer, nullable= True)
    purchase_price = Column(String, nullable= True)

    product_id = Column(Integer, ForeignKey('product.product_id'), nullable= True)
    material_id = Column(Integer, ForeignKey('material.material_id'), nullable= True)

    config_name = Column(String, nullable= True)
    config_value = Column(String, nullable= True)
    type = Column(String, nullable= True)

    internal_barcode = Column(String, nullable= True)
    registered_barcode = Column(String, nullable= True)
    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)

