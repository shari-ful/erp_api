from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import customerAddress as address_schema
from ...models import customerAddress as address_model
from ..crud.customerAddress import *
from ..crud.customer import *

address_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/customer_address", tags=['customer address'])
async def get_addresses(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_address(db=db, skip=skip, limit=limit)

@router.get("/customer_address/{address_id}", tags=['customer address'])
async def get_addresses_by_id(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address_by_id(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Customer address not found")
    return db_address

@router.post("/customer_address/create", tags=['customer address'])
async def create_addresses(address: address_schema.CreateCustomerAddress, db: Session = Depends(get_db)):
    return create_address(db=db, address=address)

@router.patch("/customer_address/update/{address_id}", tags=['customer address'])
async def update_addresses(address_id: int, address: address_schema.UpdateCustomerAddress, db: Session = Depends(get_db)):
    return update_address(db=db, address_id=address_id, address=address)

@router.delete("/customer_address/delete/{address_id}", tags=['customer address'])
async def delete_addresses(address_id: int, db: Session = Depends(get_db)):
    return delete_address(db=db, address_id=address_id)