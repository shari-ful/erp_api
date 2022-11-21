from datetime import datetime
from sqlalchemy.orm import Session
from ...models import salesOrderAddress as address_model
from ...schemas import salesOrderAddress as address_schema


#get address
def get_address(db: Session, skip: int = 0, limit: int = 50):
    return db.query(address_model.SalesOrderAddress).offset(skip).limit(limit).all()

def get_address_by_id(db: Session, address_id: int):
    return db.query(address_model.SalesOrderAddress).filter(address_model.SalesOrderAddress.address_id==address_id).first()


# create address
def create_address(db: Session, address: address_schema.CreateSalesAddress):
    new_address = address_model.SalesOrderAddress(
        sales_order_id=address.sales_order_id,
        entity_type=address.entity_type,
        first_name=address.first_name,
        last_name=address.last_name,
        company=address.company,
        phone=address.phone,
        line_1=address.line_1,
        line_2=address.line_2,
        city=address.city,
        state=address.state,
        zip=address.zip,
        country=address.country,
        created_at=datetime.now()
        )
    db.add(new_address)
    db.commit()
    return new_address

#update address info
def update_address(db: Session, address: address_schema. UpdateSalesAddress):
    address_data = db.query(address_model.SalesOrderAddress).filter(address_model.SalesOrderAddress.address_id == address.address_id).first()
    address_data.sales_order_id=address.sales_order_id,
    address_data.entity_type=address.entity_type,
    address_data.first_name=address.first_name,
    address_data.last_name=address.last_name,
    address_data.company=address.company,
    address_data.phone=address.phone,
    address_data.line_1=address.line_1,
    address_data.line_2=address.line_2,
    address_data.city=address.city,
    address_data.state=address.state,
    address_data.zip=address.zip,
    address_data.country=address.country,
    address_data.updated_at==datetime.now()
    db.commit()
    db.refresh(address_data)
    return address_data

#delete address
def delete_address(db: Session, address: address_schema.DeleteSalesAddress):
    address_data = db.query(address_model.SalesOrderAddress).filter(address_model.SalesOrderAddress.address_id == address.address_id).first()
    print(address_data)
    if not address_data:
        return None
    else:
        db.delete(address_data)
        db.commit()
        return address_data