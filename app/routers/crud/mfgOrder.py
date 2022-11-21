from datetime import datetime
from sqlalchemy.orm import Session
from ...models import mfgOrder as order_model
from ...schemas import mfgOrder as order_schema


#get mfgOrder
def get_mfg_order(db: Session, skip: int = 0, limit: int = 50):
    return db.query(order_model.MfgOrder).offset(skip).limit(limit).all()

def get_mfg_order_by_id(db: Session, mfg_order_id: int):
    return db.query(order_model.MfgOrder).filter(order_model.MfgOrder.mfg_order_id==mfg_order_id).first()


# create mfgOrder
def create_mfg_order(db: Session, mfg_order: order_schema.CreateMfgOrder):
    new_mfg_order = order_model.MfgOrder(
        status=mfg_order.status,
        order_no=mfg_order.order_no,
        variant_id=mfg_order.variant_id,
        location_id=mfg_order.location_id,
        planned_quantity=mfg_order.planned_quantity,
        actual_quantity=mfg_order.actual_quantity,
        order_created_date=mfg_order.order_created_date,
        production_deadline_date=mfg_order.production_deadline_date,
        additional_info=mfg_order.additional_info,
        created_at=datetime.now()
        )
    db.add(new_mfg_order)
    db.commit()
    return new_mfg_order

#update mfgOrder info
def update_mfg_order(db: Session, mfgOrder: order_schema.UpdateMfgOrder):
    mfg_order_data = db.query(order_model.MfgOrder).filter(order_model.MfgOrder.mfg_order_id == mfgOrder.mfg_order_id).first()
    mfg_order_data.status=mfgOrder.status,
    mfg_order_data.order_no=mfgOrder.order_no,
    mfg_order_data.variant_id=mfgOrder.variant_id,
    mfg_order_data.location_id=mfgOrder.location_id,
    mfg_order_data.order_created_date=mfgOrder.order_created_date,
    mfg_order_data.production_deadline_date=mfgOrder.production_deadline_date,
    mfg_order_data.additional_info=mfgOrder.additional_info,

    mfg_order_data.updated_at=datetime.now()

    db.commit()
    db.refresh(mfg_order_data)
    return mfg_order_data

#delete mfgOrder
def delete_mfg_order(db: Session, mfgOrder: order_schema.DeleteMfgOrder):
    mfg_order_data = db.query(order_model.MfgOrder).filter(order_model.MfgOrder.mfg_order_id == mfgOrder.mfg_order_id).first()
    print(mfg_order_data)
    if not mfg_order_data:
        return None
    else:
        db.delete(mfg_order_data)
        db.commit()
        return mfg_order_data