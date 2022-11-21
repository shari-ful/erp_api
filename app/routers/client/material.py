from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import material as material_schema
from ...models import material as material_model
from ..crud.material import *

material_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/material", tags=['material'])
async def get_materials(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_material(db=db, skip=skip, limit=limit)

@router.get("/material/{material_id}", tags=['material'])
async def get_materials_by_id(material_id: int, db: Session = Depends(get_db)):
    db_client = get_material_by_id(db, material_id=material_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.post("/material/create", tags=['material'])
async def create_materials(material: material_schema.CreateMaterial, db: Session = Depends(get_db)):
    return create_material(db=db, material=material)

@router.patch("/material/update", tags=['material'])
async def update_materials(material: material_schema.UpdateMaterial, db: Session = Depends(get_db)):
    return update_material(db=db, material=material)

@router.delete("/material/delete", tags=['material'])
async def delete_materials(material: material_schema.DeleteMaterial, db: Session = Depends(get_db)):
    return delete_material(db=db, material=material)