from datetime import datetime
from sqlalchemy.orm import Session
from ...models import material as material_model
from ...schemas import material as material_schema


#get material
def get_material(db: Session, skip: int = 0, limit: int = 50):
    return db.query(material_model.Material).offset(skip).limit(limit).all()

def get_material_by_id(db: Session, material_id: int):
    return db.query(material_model.Material).filter(material_model.Material.material_id==material_id).first()


# create material
def create_material(db: Session, material: material_schema.CreateMaterial):
    new_material = material_model.Material(
        name=material.name,
        uom=material.uom,
        default_supplier_id=material.default_supplier_id,
        type=material.type,
        additional_info=material.additional_info,
        purchase_uom=material.purchase_uom,
        purchase_uom_conversion_rate=material.purchase_uom_conversion_rate,
        batch_tracked=material.batch_tracked,
        created_at=datetime.now()
        )
    db.add(new_material)
    db.commit()
    return new_material



# #update material info
def update_material(db: Session, material: material_schema.UpdateMaterial):
    material_data = db.query(material_model.Material).filter(material_model.Material.material_id == material.material_id).first()
    material_data.name=material.name,
    material_data.uom=material.uom,
    material_data.default_supplier_id=material.default_supplier_id,
    material_data.type=material.type,
    material_data.additional_info=material.additional_info,
    material_data.purchase_uom=material.purchase_uom,
    material_data.purchase_uom_conversion_rate=material.purchase_uom_conversion_rate,
    material_data.batch_tracked=material.batch_tracked
    material_data.updated_at=datetime.now()

    db.commit()
    db.refresh(material_data)
    return material_data

# #delete material
def delete_material(db: Session, material: material_schema.DeleteMaterial):
    material_data = db.query(material_model.Material).filter(material_model.Material.material_id == material.material_id).first()
    print(material_data)
    if not material_data:
        return None
    else:
        db.delete(material_data)
        db.commit()
        return material_data