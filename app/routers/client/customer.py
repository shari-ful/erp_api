from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import customer as customer_schema
from ...models import customer as customer_model
from ..crud.customer import *

customer_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/customer", tags=['customer'])
async def get_customers(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_customer(db=db, skip=skip, limit=limit)

@router.get("/customer/{customer_id}", response_model=customer_schema.CustomerResponse,  tags=['customer'])
async def get_customers_by_id(customer_id: int, db: Session = Depends(get_db)):
    db_client = get_customer_by_id(db, customer_id=customer_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_client

@router.post("/customer/create", tags=['customer'])
async def create_customers(customer: customer_schema.Customer, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)

@router.post("/customer/quickcreate", tags=['customer'])
async def create_customers_quick(customer: customer_schema.CustomerQuickCreate, db: Session = Depends(get_db)):
    return create_customer_quick(db=db, customer=customer)

@router.patch("/customer/update{customer_id}", tags=['customer'])
async def update_customers(customer_id: int, customer: customer_schema.CustomerUpdate, db: Session = Depends(get_db)):
    return update_customer(db=db, customer_id=customer_id, customer=customer)

@router.delete("/customer/delete", tags=['customer'])
async def delete_customers(customer: customer_schema.CustomerDelete, db: Session = Depends(get_db)):
    return delete_customer(db=db, customer=customer)