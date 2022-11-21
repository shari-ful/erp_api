from sqlalchemy.orm import Session
from datetime import datetime
from ...models import customer as customer_model
from ...schemas import customer as customer_schema


#get customer
def get_customer(db: Session, skip: int = 0, limit: int = 50):
    return db.query(customer_model.Customer).offset(skip).limit(limit).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(customer_model.Customer).filter(customer_model.Customer.customer_id==customer_id).first()


# create customer
def create_customer(db: Session, customer: customer_schema.Customer):
    new_customer = customer_model.Customer(
        name=customer.name,
        first_name=customer.first_name,
        last_name=customer.last_name,
        company=customer.company,
        email=customer.email,
        phone=customer.phone,
        comment=customer.comment,
        currency=customer.currency,
        created_at=datetime.now(),
        default_billing_id=customer.default_billing_id,
        default_shipping_id=customer.default_shipping_id
        )
    db.add(new_customer)
    db.commit()
    return new_customer

def create_customer_quick(db: Session, customer: customer_schema.CustomerQuickCreate):
    new_customer = customer_model.Customer(
        email=customer.email,
        phone=customer.phone
        )
    db.add(new_customer)
    db.commit()
    return new_customer

#update customer info
def update_customer(db: Session, customer_id: int, customer: customer_schema.CustomerUpdate):
    customer_data = db.query(customer_model.Customer).filter(customer_model.Customer.customer_id == customer_id).first()
    customer_data.name=customer.name,
    customer_data.first_name=customer.first_name,
    customer_data.first_name=customer.first_name,
    customer_data.last_name=customer.last_name,
    customer_data.company=customer.company,
    customer_data.email=customer.email,
    customer_data.phone=customer.phone,
    customer_data.comment=customer.comment,
    customer_data.currency=customer.currency,
    customer_data.updated_at=datetime.now(),
    customer_data.default_billing_id=customer.default_billing_id,
    customer_data.default_shipping_id=customer.default_shipping_id
    db.commit()
    db.refresh(customer_data)
    return customer_data

#delete customer
def delete_customer(db: Session, customer: customer_schema.CustomerDelete):
    customer_data = db.query(customer_model.Customer).filter(customer_model.Customer.customer_id == customer.customer_id).first()
    print(customer_data)
    if not customer_data:
        return None
    else:
        db.delete(customer_data)
        db.commit()
        return customer_data