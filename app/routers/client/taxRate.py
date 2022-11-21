from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import taxRate as tax_rate_schema
from ...models import taxRate as tax_rate_model
from ..crud.taxRate import *

tax_rate_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/tax_rate", tags=['tax rate'])
async def get_tax_rates(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_tax_rate(db=db, skip=skip, limit=limit)

@router.get("/tax_rate/{tax_rate_id}", tags=['tax rate'])
async def get_tax_rates_by_id(tax_rate_id: int, db: Session = Depends(get_db)):
    db_client = get_tax_rate_by_id(db, tax_rate_id=tax_rate_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Tax rate not found")
    return db_client

@router.post("/tax_rate/create", tags=['tax rate'])
async def create_tax_rates(tax_rate: tax_rate_schema.CreateTaxRate, db: Session = Depends(get_db)):
    return create_tax_rate(db=db, tax_rate=tax_rate)

