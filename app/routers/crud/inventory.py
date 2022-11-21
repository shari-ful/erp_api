from sqlalchemy.orm import Session
from ...models import inventory as inventory_model
from ...schemas import inventory as inventory_schema


#get inventory
def get_inventory(db: Session, skip: int = 0, limit: int = 50):
    return db.query(inventory_model.Inventory).offset(skip).limit(limit).all()

def get_inventory_by_id(db: Session, inventory_id: int):
    return db.query(inventory_model.Inventory).filter(inventory_model.Inventory.inventory_id==inventory_id).first()


# create inventory
def create_inventory(db: Session, inventory: inventory_schema.CreateInventory):
    new_inventory = inventory_model.Inventory(
        location_id=inventory.location_id,
        variant_id=inventory.variant_id,
        value=inventory.value
        )
    db.add(new_inventory)
    db.commit()
    return new_inventory

#update inventory info
def update_inventory(db: Session, inventory: inventory_schema.UpdateInventory):
    inventory_data = db.query(inventory_model.Inventory).filter(inventory_model.Inventory.inventory_id == inventory.inventory_id).first()
    inventory_data.location_id=inventory.location_id,
    inventory_data.variant_id=inventory.variant_id,
    inventory_data.value=inventory.value

    db.commit()
    db.refresh(inventory_data)
    return inventory_data

#delete inventory
def delete_inventory(db: Session, inventory: inventory_schema.DeleteInventory):
    inventory_data = db.query(inventory_model.Inventory).filter(inventory_model.Inventory.inventory_id == inventory.inventory_id).first()
    print(inventory_data)
    if not inventory_data:
        return None
    else:
        db.delete(inventory_data)
        db.commit()
        return inventory_data