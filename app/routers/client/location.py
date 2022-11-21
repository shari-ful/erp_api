from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import location as location_schema
from ...models import location as location_model
from ..crud.location import *

location_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/location", tags=['location'])
async def get_locations(skip: int=0, limit: int=50, db: Session = Depends(get_db)):
    return get_location(db=db, skip=skip, limit=limit)

@router.get("/location/{location_id}", tags=['location'])
async def get_locations_by_id(location_id: int, db: Session = Depends(get_db)):
    db_location = get_location_by_id(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@router.post("/location/create", tags=['location'])
async def create_locations(location: location_schema.CreateLocation, db: Session = Depends(get_db)):
    return create_location(db=db, location=location)

@router.patch("/location/update", tags=['location'])
async def update_locations(location: location_schema.UpdateLocation, db: Session = Depends(get_db)):
    return update_location(db=db, location=location)

@router.delete("/location/delete", tags=['location'])
async def delete_locations(location: location_schema.DeleteLocation, db: Session = Depends(get_db)):
    return delete_location(db=db, location=location)