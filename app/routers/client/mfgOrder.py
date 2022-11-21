from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import mfgOrder as mfg_order_schema
from ...models import mfgOrder as mfg_order_model
from ..crud.mfgOrder import *

mfg_order_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/mfg_order", tags=['mfg order'])
async def get_mfgOrders(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_mfg_order(db=db, skip=skip, limit=limit)

@router.get("/mfg_order/{mfg_rder_id}", tags=['mfg order'])
async def get_mfgOrders_by_id(mfg_order_id: int, db: Session = Depends(get_db)):
    db_client = get_mfg_order_by_id(db, mfg_order_id=mfg_order_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="mfg order not found")
    return db_client

@router.post("/mfg_order/create", tags=['mfg order'])
async def create_mfgOrders(mfg_order: mfg_order_schema.CreateMfgOrder, db: Session = Depends(get_db)):
    return create_mfg_order(db=db, mfg_order=mfg_order)

@router.patch("/mfg_order/update", tags=['mfg order'])
async def update_mfg_order(mfg_order: mfg_order_schema.UpdateMfgOrder, db: Session = Depends(get_db)):
    return update_mfg_order(db=db, mfg_order=mfg_order)

@router.delete("/mfg_order/delete", tags=['mfg order'])
async def delete_mfg_order(mfg_order: mfg_order_schema.DeleteMfgOrder, db: Session = Depends(get_db)):
    return delete_mfg_order(db=db, mfg_order=mfg_order)