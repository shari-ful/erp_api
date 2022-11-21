from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import purchaseOrder as order_schema
from ...models import purchaseOrder as order_model
from ..crud.purchaseOrder import *

order_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/purchase_order", tags=['purchase order'])
async def get_orders(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_order(db=db, skip=skip, limit=limit)

@router.get("/purchase_order/{order_id}", tags=['purchase order'])
async def get_orders_by_id(order_id: int, db: Session = Depends(get_db)):
    db_client = get_order_by_id(db, order_id=order_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="purchase order not found")
    return db_client

@router.post("/purchase_order/create", tags=['purchase order'])
async def create_orders(order: order_schema.CreatePurchaseOrder, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)


@router.patch("/purchase_order/update", tags=['purchase order'])
async def update_orders(order: order_schema.UpdatePurchaseOrder, db: Session = Depends(get_db)):
    return update_order(db=db, order=order)

@router.delete("/purchase_order/delete", tags=['purchase order'])
async def delete_orders(order: order_schema.DeletePurchaseOrder, db: Session = Depends(get_db)):
    return delete_order(db=db, order=order)