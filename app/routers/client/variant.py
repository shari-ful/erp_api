from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import variant as variant_schema
from ...models import variant as variant_model
from ..crud.variant import *

variant_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/variant", tags=['variant'])
async def get_variants(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_variant(db=db, skip=skip, limit=limit)

@router.get("/variant/{variant_id}", tags=['variant'])
async def get_variants_by_id(variant_id: int, db: Session = Depends(get_db)):
    db_variant = get_variant_by_id(db, variant_id=variant_id)
    if db_variant is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return db_variant

@router.post("/variant/create", tags=['variant'])
async def create_variants(variant: variant_schema.CreateVariant, db: Session = Depends(get_db)):
    return create_variant(db=db, variant=variant)

@router.patch("/variant/update", tags=['variant'])
async def update_variants(variant: variant_schema.UpdateVariant, db: Session = Depends(get_db)):
    return update_variant(db=db, variant=variant)

@router.delete("/variant/delete/{variant_id}", tags=['variant'])
async def delete_variants(variant_id: int, variant: variant_schema.DeleteVariant, db: Session = Depends(get_db)):
    db_variant = get_variant_by_id(db, variant_id=variant_id)
    if db_variant is None:
        raise HTTPException(status_code=404, detail="Variant not found")
    return delete_variant(db=db, variant=variant)