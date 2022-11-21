from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import salesOrderRow as row_schema
from ...models import salesOrderRow as row_model
from ..crud.salesOrderRow import *

row_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/sales_order_row", tags=['sales order row'])
async def get_order_rows(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_order_row(db=db, skip=skip, limit=limit)

@router.get("/sales_order_row/{sales_order_row_id}", tags=['sales order row'])
async def get_rows_by_id(sales_order_row_id: int, db: Session = Depends(get_db)):
    db_client = get_row_by_id(db, sales_order_row_id=sales_order_row_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Sales order not found")
    return db_client

@router.post("/sales_order_row/create", tags=['sales order row'])
async def create_order_rows(order_row: row_schema.CreateSalesOrderRow, db: Session = Depends(get_db)):
    return create_order_row(db=db, order_row=order_row)


@router.patch("/sales_order_row/update", tags=['sales order row'])
async def update_order_rows(order_row: row_schema.UpdateSalesOrderRow, db: Session = Depends(get_db)):
    return update_order_row(db=db, order_row=order_row)

@router.delete("/sales_order_row/delete", tags=['sales order row'])
async def delete_order_rows(order_row: row_schema.DeleteSalesOrderRow, db: Session = Depends(get_db)):
    return delete_order_row(db=db, order_row=order_row)