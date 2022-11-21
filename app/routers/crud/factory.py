from urllib import response
from sqlalchemy.orm import Session
from ...models import customer as customer_model, customerAddress as address_model
from ...schemas import customer as customer_schema, customerAddress as address_schema


# retrive factory
def get_factory(db: Session):
    customer = db.query(customer_model.Customer).all()
    address = db.query(address_model.CustomerAddress).all()
    response_model = customer
    return response_model