from datetime import datetime
from sqlalchemy.orm import Session
from ...models import salesOrder as order_model
from ...schemas import salesOrder as order_schema


#get salesOrder
def get_salesOrder(db: Session, skip: int = 0, limit: int = 50):
    return db.query(order_model.SalesOrder).offset(skip).limit(limit).all()

def get_salesOrder_by_id(db: Session, sales_order_id: int):
    return db.query(order_model.SalesOrder).filter(order_model.SalesOrder.sales_order_id==sales_order_id).first()


# create salesOrder
def create_salesOrder(db: Session, salesOrder: order_schema.CreateSalesOrder):
    new_sales_order = order_model.SalesOrder(
        order_no=salesOrder.order_no,
        customer_id=salesOrder.customer_id,
        tracking_number=salesOrder.tracking_number,
        tracking_number_url=salesOrder.tracking_number_url,
        order_created_date=salesOrder.order_created_date,
        delivery_date=salesOrder.delivery_date,
        currency=salesOrder.currency,
        location_id=salesOrder.location_id,
        status=salesOrder.status,
        additional_info=salesOrder.additional_info,
        created_at=datetime.now()
        )
    db.add(new_sales_order)
    db.commit()
    return new_sales_order

#update salesOrder info
def update_salesOrder(db: Session, salesOrder: order_schema.UpdateSalesOrder):
    salesOrder_data = db.query(order_model.SalesOrder).filter(order_model.SalesOrder.sales_order_id == salesOrder.sales_order_id).first()
    salesOrder_data.tracking_number=salesOrder.tracking_number,
    salesOrder_data.tracking_number_url=salesOrder.tracking_number_url,
    salesOrder_data.delivery_date=salesOrder.delivery_date,
    salesOrder_data.currency=salesOrder.currency,
    salesOrder_data.status=salesOrder.status,
    salesOrder_data.updated_at=datetime.now()

    db.commit()
    db.refresh(salesOrder_data)
    return salesOrder_data

#delete salesOrder
def delete_salesOrder(db: Session, salesOrder: order_schema.DeleteSalesOrder):
    salesOrder_data = db.query(order_model.SalesOrder).filter(order_model.SalesOrder.sales_order_id == salesOrder.sales_order_id).first()
    print(salesOrder_data)
    if not salesOrder_data:
        return None
    else:
        db.delete(salesOrder_data)
        db.commit()
        return salesOrder_data