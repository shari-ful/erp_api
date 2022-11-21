from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import mfgOrderOperation as operation_schema
from ...models import mfgOrderOperation as operation_model
from ..crud.mfgOrderOperation import *

operation_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/mfg_order_operation", tags=['mfg order operation'])
async def get_operations(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_operation(db=db, skip=skip, limit=limit)

@router.get("/mfg_order_operation/{mfg_rder_id}", tags=['mfg order operation'])
async def get_operations_by_id(mfg_order_id: int, db: Session = Depends(get_db)):
    db_client = get_operation_by_id(db, mfg_order_id=mfg_order_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="mfg order operation not found")
    return db_client

@router.post("/mfg_order_operation/create", tags=['mfg order operation'])
async def create_operations(mfg_order: operation_schema.CreateMfgOrderOperation, db: Session = Depends(get_db)):
    return create_operation(db=db, mfg_order=mfg_order)

@router.patch("/mfg_order_operation/update", tags=['mfg order operation'])
async def update_operations(mfg_order: operation_schema.UpdateMfgOrderOperation, db: Session = Depends(get_db)):
    return update_operation(db=db, mfg_order=mfg_order)

@router.delete("/mfg_order_operation/delete", tags=['mfg order operation'])
async def delete_operations(mfg_order: operation_schema.DeleteMfgOrderOperation, db: Session = Depends(get_db)):
    return delete_operation(db=db, mfg_order=mfg_order)