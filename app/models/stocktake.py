from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..config.dbpostgres import Base

class Stocktake(Base):
    __tablename__ = 'stocktake'
    stocktake_id = Column(Integer, primary_key=True, index=True)
    stocktake_number = Column(String(50), nullable= True)

    location_id = Column(String(10), nullable= True)

    status = Column(String(50), nullable= True)
    reason = Column(String(250), nullable= True)
    
    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)