from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class MfgOrder(Base):
    __tablename__= 'mfg_order'
    
    mfg_order_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable = True)
    order_no = Column(String(50), nullable = True)
    variant_id = Column(Integer, ForeignKey("variant.variant_id"), nullable = True)
    planned_quantity = Column(Integer, nullable = True)
    actual_quantity = Column(Integer, nullable = True)
    batch_transactions = Column(String(50), nullable = True)

    batch_id = Column(Integer, ForeignKey("batch.batch_id"), nullable = True)
    quantity = Column(Integer, nullable = True)
    location_id = Column(Integer, nullable = True)

    order_created_date = Column(String(50), nullable = True)
    done_date = Column(String(50), nullable = True)
    production_deadline_date = Column(String(50), nullable = True)
    additional_info = Column(String(200), nullable = True)
    is_linked_to_sales_order = Column(Boolean, nullable = True)

    sales_order_id = Column(Integer, ForeignKey("sales_order.sales_order_id"), nullable = True)
    sales_order_row_id = Column(Integer, ForeignKey("sales_order_row.sales_order_row_id"), nullable = True)

    sales_order_delivery_deadline = Column(String(50), nullable = True)
    ingredient_availability = Column(String(50), nullable = True)
    total_cost = Column(Float, nullable = True)
    total_planned_time = Column(String(50), nullable = True)
    total_actual_time = Column(String(50), nullable = True)
    material_cost = Column(Float, nullable = True)
    subassemblies_cost = Column(Float, nullable = True)
    operations_cost = Column(Float, nullable = True)

    created_at = Column(DateTime, nullable= True)
    updated_at = Column(DateTime, nullable= True)

