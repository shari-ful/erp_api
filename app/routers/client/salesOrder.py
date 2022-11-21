from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import salesOrder as salesOrder_schema
from ...models import salesOrder as salesOrder_model
from ..crud.salesOrder import *

salesOrder_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/sales_order", tags=['sales order'])
async def get_salesOrders(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_salesOrder(db=db, skip=skip, limit=limit)

@router.get("/sales_order/{sales_order_id}", tags=['sales order'])
async def get_salesOrders_by_id(sales_order_id: int, db: Session = Depends(get_db)):
    db_client = get_salesOrder_by_id(db, sales_order_id=sales_order_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Sales order not found")
    return db_client

@router.post("/sales_order/create", tags=['sales order'])
async def create_salesOrders(salesOrder: salesOrder_schema.CreateSalesOrder, db: Session = Depends(get_db)):
    return create_salesOrder(db=db, salesOrder=salesOrder)


@router.patch("/sales_order/update", tags=['sales order'])
async def update_salesOrders(salesOrder: salesOrder_schema.UpdateSalesOrder, db: Session = Depends(get_db)):
    return update_salesOrder(db=db, salesOrder=salesOrder)

@router.delete("/sales_order/delete", tags=['sales order'])
async def delete_salesOrders(salesOrder: salesOrder_schema.DeleteSalesOrder, db: Session = Depends(get_db)):
    return delete_salesOrder(db=db, salesOrder=salesOrder)