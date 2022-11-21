from numbers import Number
from sqlalchemy import Column, Integer, Float, DateTime
from ..config.dbpostgres import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True, index=True)

    location_id = Column(Integer, nullable= True)
    variant_id = Column(Integer, nullable= True)
    value = Column(Float, nullable= True)

    created_at = Column(DateTime, nullable= True)
    updated_at = Column(DateTime, nullable= True)
 