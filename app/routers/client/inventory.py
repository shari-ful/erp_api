from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import inventory as inventory_schema
from ...models import inventory as inventory_model
from ..crud.inventory import *

inventory_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/inventory", tags=['inventory'])
async def get_inventorys(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_inventory(db=db, skip=skip, limit=limit)

@router.get("/inventory/{inventory_id}", tags=['inventory'])
async def get_inventorys_by_id(inventory_id: int, db: Session = Depends(get_db)):
    db_inventory = get_inventory_by_id(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.post("/inventory/create", tags=['inventory'])
async def create_inventorys(inventory: inventory_schema.CreateInventory, db: Session = Depends(get_db)):
    return create_inventory(db=db, inventory=inventory)

@router.patch("/inventory/update", tags=['inventory'])
async def update_inventorys(inventory: inventory_schema.UpdateInventory, db: Session = Depends(get_db)):
    return update_inventory(db=db, inventory=inventory)

@router.delete("/inventory/delete", tags=['inventory'])
async def delete_inventorys(inventory: inventory_schema.DeleteInventory, db: Session = Depends(get_db)):
    return delete_inventory(db=db, inventory=inventory)