from sqlalchemy.orm import Session
from ...models import variant as variant_model
from ...schemas import variant as variant_schema


#get variant
def get_variant(db: Session, skip: int = 0, limit: int = 50):
    return db.query(variant_model.Variant).offset(skip).limit(limit).all()

def get_variant_by_id(db: Session, variant_id: int):
    return db.query(variant_model.Variant).filter(variant_model.Variant.variant_id==variant_id).first()


# create variant
def create_variant(db: Session, variant: variant_schema.CreateVariant):
    try:
        new_variant = variant_model.Variant(
            sku=variant.sku,
            sales_price=variant.sales_price,
            purchase_price=variant.purchase_price,
            product_id=variant.product_id,
            internal_barcode=variant.internal_barcode,
            registered_barcode=variant.registered_barcode,
            material_id=variant.material_id)
  
        db.add(new_variant)
        db.commit()
        db.refresh(new_variant)
        return new_variant
    except Exception as e:
        return e

#update variant info
def update_variant(db: Session, variant: variant_schema.UpdateVariant):
    variant_data = db.query(variant_model.Variant).filter(variant_model.Variant.variant_id == variant.variant_id).first()
    variant_data.sku=variant.sku,
    variant_data.sales_price=variant.sales_price,
    variant_data.purchase_price=variant.purchase_price,
    variant_data.product_id=variant.product_id,
    variant_data.internal_barcode=variant.internal_barcode,
    variant_data.registered_barcode=variant.registered_barcode,
    variant_data.material_id=variant.material_id

    db.commit()
    db.refresh(variant_data)
    return variant_data

#delete variant
def delete_variant(db: Session, variant: variant_schema.DeleteVariant):
    variant_data = db.query(variant_model.Variant).filter(variant_model.Variant.variant_id == variant.variant_id).first()
    if not variant_data:
        return None
    else:
        db.delete(variant_data)
        db.commit()
        return variant_data
