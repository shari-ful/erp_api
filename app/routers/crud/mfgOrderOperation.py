from datetime import datetime
from sqlalchemy.orm import Session
from ...models import mfgOrderOperation as operation_model
from ...schemas import mfgOrderOperation as operation_schema


#get mfg order operation
def get_operation(db: Session, skip: int = 0, limit: int = 50):
    return db.query(operation_model.MfgOrderOperation).offset(skip).limit(limit).all()

def get_operation_by_id(db: Session, operation_id: int):
    return db.query(operation_model.MfgOrderOperation).filter(operation_model.MfgOrderOperation.operation_id==operation_id).first()


# create mfg order operation
def create_operation(db: Session, mfg_order: operation_schema.CreateMfgOrderOperation):
    new_operation = operation_model.MfgOrderOperation(
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
    db.add(new_operation)
    db.commit()
    return new_operation

#update mfg order operation info
def update_operation(db: Session, mfgOrderOperation: operation_schema.UpdateMfgOrderOperation):
    operation_data = db.query(operation_model.MfgOrderOperation).filter(operation_model.MfgOrderOperation.operation_id == mfgOrderOperation.operation_id).first()
    operation_data.status=mfgOrderOperation.status,
    operation_data.order_no=mfgOrderOperation.order_no,
    operation_data.variant_id=mfgOrderOperation.variant_id,
    operation_data.location_id=mfgOrderOperation.location_id,
    operation_data.order_created_date=mfgOrderOperation.order_created_date,
    operation_data.production_deadline_date=mfgOrderOperation.production_deadline_date,
    operation_data.additional_info=mfgOrderOperation.additional_info,

    operation_data.updated_at=datetime.now()

    db.commit()
    db.refresh(operation_data)
    return operation_data

#delete mfg order operation
def delete_operation(db: Session, operation: operation_schema.DeleteMfgOrderOperation):
    operation_data = db.query(operation_model.MfgOrderOperation).filter(operation_model.MfgOrderOperation.operation_id == mfgOrderOperation.operation_id).first()
    print(operation_data)
    if not operation_data:
        return None
    else:
        db.delete(operation_data)
        db.commit()
        return operation_data