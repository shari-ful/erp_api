from datetime import datetime
from sqlalchemy.orm import Session
from ...models import location as location_model
from ...schemas import location as location_schema


#get location
def get_location(db: Session, skip: int = 0, limit: int = 50):
    return db.query(location_model.Location).offset(skip).limit(limit).all()

def get_location_by_id(db: Session, location_id: int):
    return db.query(location_model.Location).filter(location_model.Location.location_id==location_id).first()


# create location
def create_location(db: Session, location: location_schema.CreateLocation):
    new_location = location_model.Location(
        name=location.name,
        legal_name=location.legal_name,
        address_id=location.address_id,
        is_primary=location.is_primary,
        sales_allowed=location.sales_allowed,
        manufacturing_allowed=location.manufacturing_allowed,
        purchase_allowed=location.purchase_allowed,
        created_at=datetime.now()
        )
    db.add(new_location)
    db.commit()
    return new_location


# #update location info
def update_location(db: Session, location: location_schema.UpdateLocation):
    location_data = db.query(location_model.Location).filter(location_model.Location.location_id == location.location_id).first()
    location_data.name=location.name,
    location_data.legal_name=location.legal_name,
    location_data.address_id=location.address_id,
    location_data.is_primary=location.is_primary,
    location_data.sales_allowed=location.sales_allowed,
    location_data.manufacturing_allowed=location.manufacturing_allowed,
    location_data.purchase_allowed=location.purchase_allowed,
    location_data.updated_at=datetime.now()

    db.commit()
    db.refresh(location_data)
    return location_data

# #delete location
def delete_location(db: Session, location: location_schema.DeleteLocation):
    location_data = db.query(location_model.Location).filter(location_model.Location.location_id == location.location_id).first()
    if not location_data:
        return None
    else:
        db.delete(location_data)
        db.commit()
        return location_data