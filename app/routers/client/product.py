from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import product as product_schema
from ...models import product as product_model
from ..crud.product import *

product_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/product", tags=['product'])
async def get_products(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_product(db=db, skip=skip, limit=limit)

@router.get("/product/{product_id}", tags=['product'])
async def get_products_by_id(product_id: int, db: Session = Depends(get_db)):
    db_client = get_product_by_id(db, product_id=product_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.post("/product/create", tags=['product'])
async def create_products(product: product_schema.CreateProduct, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.patch("/product/update", tags=['product'])
async def update_products(product: product_schema.UpdateProduct, db: Session = Depends(get_db)):
    return update_product(db=db, product=product)

@router.delete("/product/delete", tags=['product'])
async def delete_products(product: product_schema.DeleteProduct, db: Session = Depends(get_db)):
    return delete_product(db=db, product=product)