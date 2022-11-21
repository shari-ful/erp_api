from datetime import datetime
from sqlalchemy.orm import Session
from ...models import purchaseOrder as order_model
from ...schemas import purchaseOrder as order_schema


#get order
def get_order(db: Session, skip: int = 0, limit: int = 50):
    return db.query(order_model.PurchaseOrder).offset(skip).limit(limit).all()

def get_order_by_id(db: Session, purchase_order_id: int):
    return db.query(order_model.PurchaseOrder).filter(order_model.PurchaseOrder.purchase_order_id==purchase_order_id).first()


# create order
def create_order(db: Session, order: order_schema.CreatePurchaseOrder):
    new_order = order_model.Order(
        order_no=order.order_no,
        entity_type=order.entity_type,
        status=order.status,
        supplier_id=order.supplier_id,
        location_id=order.location_id,
        currency=order.currency,
        expected_arrival_date=order.expected_arrival_date,
        order_created_date=order.order_created_date,
        tracking_location_id=order.tracking_location_id,
        additional_info=order.additional_info,
        created_at=datetime.now()
        )
    db.add(new_order)
    db.commit()
    return new_order

#update order info
def update_order(db: Session, order: order_schema.UpdatePurchaseOrder):
    order_data = db.query(order_model.Order).filter(order_model.PurchaseOrder.purchase_order_id == order.order_id).first()
    order_data.order_no=order.order_no,
    order_data.entity_type=order.entity_type,
    order_data.status=order.status,
    order_data.supplier_id=order.supplier_id,
    order_data.location_id=order.location_id,
    order_data.currency=order.currency,
    order_data.expected_arrival_date=order.expected_arrival_date,
    order_data.order_created_date=order.order_created_date,
    order_data.tracking_location_id=order.tracking_location_id,
    order_data.additional_info=order.additional_info,
    order_data.updated_at=datetime.now()

    db.commit()
    db.refresh(order_data)
    return order_data

#delete order
def delete_order(db: Session, order: order_schema.DeletePurchaseOrder):
    order_data = db.query(order_model.PurchaseOrder).filter(order_model.PurchaseOrder.purchase_order_id == order.order_id).first()
    print(order_data)
    if not order_data:
        return None
    else:
        db.delete(order_data)
        db.commit()
        return order_data