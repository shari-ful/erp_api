from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import supplier as supplier_schema
from ...models import supplier as supplier_model
from ..crud.supplier import *

supplier_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/supplier", tags=['supplier'])
async def get_suppliers(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_supplier(db=db, skip=skip, limit=limit)

@router.get("/supplier/{supplier_id}", tags=['supplier'])
async def get_suppliers_by_id(supplier_id: int, db: Session = Depends(get_db)):
    db_client = get_supplier_by_id(db, supplier_id=supplier_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_client

@router.post("/supplier/create", tags=['supplier'])
async def create_suppliers(supplier: supplier_schema.CreateSupplier, db: Session = Depends(get_db)):
    return create_supplier(db=db, supplier=supplier)


@router.patch("/supplier/update", tags=['supplier'])
async def update_suppliers(supplier: supplier_schema.UpdateSupplier, db: Session = Depends(get_db)):
    return update_supplier(db=db, supplier=supplier)

@router.delete("/supplier/delete", tags=['supplier'])
async def delete_suppliers(supplier: supplier_schema.DeleteSupplier, db: Session = Depends(get_db)):
    return delete_supplier(db=db, supplier=supplier)