from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class MfgOrderOperation(Base):
    __tablename__= 'mfg_order_recipe'
    
    mfg_recipe_id = Column(Integer, primary_key=True, index=True)
    mfg_order_id = Column(Integer, ForeignKey("mfg_order.mfg_order_id"), nullable = True)
    variant_id = Column(Integer, ForeignKey("variant.variant_id"), nullable = True)
    notes = Column(String(200), nullable = True)
    planned_quantity_per_unit = Column(Integer, nullable = True)
    total_actual_quantity = Column(Integer, nullable = True)
    ingredient_availability = Column(String(50), nullable = True)
    ingredient_expected_date = Column(String(50), nullable = True)
    cost = Column(Float, nullable = True)

    created_at = Column(DateTime, nullable= True)
    updated_at = Column(DateTime, nullable= True)

