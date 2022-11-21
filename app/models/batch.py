from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..config.dbpostgres import Base

class Batch(Base):
    __tablename__ = 'batch'
    batch_id = Column(Integer, primary_key=True, index=True)
    batch_number = Column(String, nullable= True)
    expiration_date = Column(String, nullable= True)
    batch_created_date = Column(String, nullable= True)

    variant_id = Column(Integer, ForeignKey("variant.variant_id"), nullable= True)
    
    batch_barcode = Column(String, nullable= True)

    created_at = Column(DateTime, nullable = True)
    updated_at = Column(DateTime, nullable = True)