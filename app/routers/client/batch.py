from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import batch as batch_schema
from ...models import batch as batch_model
from ..crud.batch import *

batch_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/batch", tags=['batch'])
async def get_batchs(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_batch(db=db, skip=skip, limit=limit)

@router.get("/batch/{batch_id}", tags=['batch'])
async def get_batchs_by_id(batch_id: int, db: Session = Depends(get_db)):
    db_batch = get_batch_by_id(db, batch_id=batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

@router.post("/batch/create", tags=['batch'])
async def create_batchs(batch: batch_schema.CreateBatch, db: Session = Depends(get_db)):
    return create_batch(db=db, batch=batch)


@router.patch("/batch/update/{batch_id}", tags=['batch'])
async def update_batchs(batch_id: int, batch: batch_schema.UpdateBatch, db: Session = Depends(get_db)):
    return update_batch(db=db, batch_id=batch_id, batch=batch)

@router.delete("/batch/delete/{batch_id}", tags=['batch'])
async def delete_batchs(batch_id: int, db: Session = Depends(get_db)):
    db_batch = get_batch_by_id(db, batch_id=batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return delete_batch(db=db, batch_id=batch_id)