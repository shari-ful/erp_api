from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class SalesOrderRow(Base):
    __tablename__ = 'sales_order_row'
    sales_order_row_id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable= True)

    batch_id = Column(Integer, ForeignKey("batch.batch_id"), nullable= True)
    variant_id = Column(Integer, ForeignKey("variant.variant_id"), nullable= True)
    tax_rate_id = Column(Integer, ForeignKey("tax_rate.tax_rate_id"), nullable= True)

    price_per_unit = Column(Float, nullable= True)
    price_per_unit_in_base_currency = Column(Float, nullable= True)
    total = Column(Integer, nullable= True)
    total_in_base_currency = Column(Integer, nullable= True)

    quantity = Column(Integer, nullable= True)
    conversion_rate = Column(Integer, nullable= True)
    conversion_date = Column(Integer, nullable= True)

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)