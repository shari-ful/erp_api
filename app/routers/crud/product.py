from sqlalchemy.orm import Session
from ...models import product as product_model
from ...schemas import product as product_schema


#get product
def get_product(db: Session, skip: int = 0, limit: int = 50):
    return db.query(product_model.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(product_model.Product).filter(product_model.Product.product_id==product_id).first()


# create product
def create_product(db: Session, product: product_schema.CreateProduct):
    new_product = product_model.Product(
        uom=product.uom,
        name=product.name,
        is_producible=product.is_producible,
        is_purchasable=product.is_purchasable,
        default_supplier_id=product.default_supplier_id,
        additional_info=product.additional_info,
        batch_tracked=product.batch_tracked,
        purchase_uom=product.purchase_uom,
        purchase_uom_conversion_rate=product.purchase_uom_conversion_rate        
        )
    db.add(new_product)
    db.commit()
    return new_product


# #update product info
def update_product(db: Session, product: product_schema.UpdateProduct):
    product_data = db.query(product_model.Product).filter(product_model.Product.product_id == product.product_id).first()
    product_data.uom=product.uom,
    product_data.name=product.name,
    product_data.is_producible=product.is_producible,
    product_data.is_purchasable=product.is_purchasable,
    product_data.default_supplier_id=product.default_supplier_id,
    product_data.additional_info=product.additional_info,
    product_data.batch_tracked=product.batch_tracked,
    product_data.purchase_uom=product.purchase_uom,
    product_data.purchase_uom_conversion_rate=product.purchase_uom_conversion_rate

    db.commit()
    db.refresh(product_data)
    return product_data

# #delete product
def delete_product(db: Session, product: product_schema.DeleteProduct):
    product_data = db.query(product_model.Product).filter(product_model.Product.product_id == product.product_id).first()
    if not product_data:
        return None
    else:
        db.delete(product_data)
        db.commit()
        return product_data