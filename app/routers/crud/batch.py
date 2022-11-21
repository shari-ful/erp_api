from sqlalchemy.orm import Session
from ...models import batch as batch_model
from ...schemas import batch as batch_schema


#get batch
def get_batch(db: Session, skip: int = 0, limit: int = 50):
    return db.query(batch_model.Batch).offset(skip).limit(limit).all()

def get_batch_by_id(db: Session, batch_id: int):
    return db.query(batch_model.Batch).filter(batch_model.Batch.batch_id==batch_id).first()


# create batch
def create_batch(db: Session, batch: batch_schema.CreateBatch):
    try:
        new_batch = batch_model.Batch(
            batch_number=batch.batch_number,
            expiration_date=batch.expiration_date,
            batch_created_date=batch.batch_created_date,
            variant_id=batch.variant_id,
            batch_barcode=batch.batch_barcode)
  
        db.add(new_batch)
        db.commit()
        db.refresh(new_batch)
        return new_batch
    except Exception as e:
        return e

#update batch info
def update_batch(db: Session, batch_id: int, batch: batch_schema.UpdateBatch):
    batch_data = db.query(batch_model.Batch).filter(batch_model.Batch.batch_id == batch_id).first()
    batch_data.batch_number=batch.batch_number
    batch_data.expiration_date=batch.expiration_date,
    batch_data.batch_created_date=batch.batch_created_date,
    batch_data.batch_barcode=batch.batch_barcode

    db.commit()
    db.refresh(batch_data)
    return batch_data

#delete batch
def delete_batch(db: Session, batch_id: int):
    batch_data = db.query(batch_model.Batch).filter(batch_model.Batch.batch_id == batch_id).first()
    if not batch_data:
        return None
    else:
        db.delete(batch_data)
        db.commit()
        return batch_data
