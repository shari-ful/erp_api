from datetime import datetime
from sqlalchemy.orm import Session
from ...models import supplier as supplier_model
from ...schemas import supplier as supplier_schema


#get supplier
def get_supplier(db: Session, skip: int = 0, limit: int = 50):
    return db.query(supplier_model.Supplier).offset(skip).limit(limit).all()

def get_supplier_by_id(db: Session, supplier_id: int):
    return db.query(supplier_model.Supplier).filter(supplier_model.Supplier.supplier_id==supplier_id).first()


# create supplier
def create_supplier(db: Session, supplier: supplier_schema.CreateSupplier):
    new_supplier = supplier_model.Supplier(
        name=supplier.name,
        currency=supplier.currency,
        email=supplier.email,
        comment=supplier.comment,
        created_at=datetime.now()
        )
    db.add(new_supplier)
    db.commit()
    return new_supplier

#update supplier info
def update_supplier(db: Session, supplier: supplier_schema.UpdateSupplier):
    supplier_data = db.query(supplier_model.Supplier).filter(supplier_model.Supplier.supplier_id == supplier.supplier_id).first()
    supplier_data.name=supplier.name,
    supplier_data.currency=supplier.currency,
    supplier_data.email=supplier.email,
    supplier_data.comment=supplier.comment,
    supplier_data.updated_at=datetime.now()

    db.commit()
    db.refresh(supplier_data)
    return supplier_data

#delete supplier
def delete_supplier(db: Session, supplier: supplier_schema.DeleteSupplier):
    supplier_data = db.query(supplier_model.Supplier).filter(supplier_model.Supplier.supplier_id == supplier.supplier_id).first()
    print(supplier_data)
    if not supplier_data:
        return None
    else:
        db.delete(supplier_data)
        db.commit()
        return supplier_data