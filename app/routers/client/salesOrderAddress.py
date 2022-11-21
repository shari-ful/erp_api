from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import salesOrderAddress as address_schema
from ...models import salesOrderAddress as address_model
from ..crud.salesOrderAddress import *

address_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/sales_address", tags=['sales order address'])
async def get_addresses(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_address(db=db, skip=skip, limit=limit)

@router.get("/sales_address/{address_id}", tags=['sales order address'])
async def get_addresses_by_id(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address_by_id(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return get_address_by_id(db, address_id=address_id)

@router.post("/sales_address/create", tags=['sales order address'])
async def create_addresses(address: address_schema.CreateSalesAddress, db: Session = Depends(get_db)):
    return create_address(db=db, address=address)

@router.patch("/sales_address/update", tags=['sales order address'])
async def update_addresses(address: address_schema.UpdateSalesAddress, db: Session = Depends(get_db)):
    return update_address(db=db, address=address)

@router.delete("/sales_address/delete", tags=['sales order address'])
async def delete_addresses(address: address_schema.DeleteSalesAddress, db: Session = Depends(get_db)):
    return delete_address(db=db, address=address)