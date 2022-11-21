from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class MfgOrderOperation(Base):
    __tablename__= 'mfg_order_operation'
    
    mfg_operation_id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable = True)
    rank = Column(Integer, nullable = True)
    mfg_order_id = Column(Integer, ForeignKey("mfg_order.mfg_order_id"), nullable = True)
    
    operation_id = Column(Integer, ForeignKey("operation.operation_id"), nullable = True)
    operation_name = Column(String(50), ForeignKey("operation.operation_name"), nullable = True)
    resource_id = Column(Integer, ForeignKey("resource.resource_id"), nullable = True)
    resource_name = Column(String(50), ForeignKey("resource.resource_name"), nullable = True)
    
    assigned_operators = Column(String(50), nullable = True)
    planned_time_per_unit = Column(Integer, nullable = True)
    total_actual_time = Column(Integer, nullable = True)
    planned_cost_per_unit = Column(String(50), nullable = True)
    total_actual_cost = Column(Float, nullable = True)
    cost_per_hour = Column(Float, nullable = True)
    completed_at = Column(String(50), nullable = True)

    created_at = Column(DateTime, nullable= True)
    updated_at = Column(DateTime, nullable= True)

