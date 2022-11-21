from datetime import datetime
from sqlalchemy.orm import Session
from ...models import salesOrderRow as row_model
from ...schemas import salesOrderRow as row_schema

#get order_row
def get_order_row(db: Session, skip: int = 0, limit: int = 50):
    return db.query(row_model.SalesOrderRow).offset(skip).limit(limit).all()

def get_row_by_id(db: Session, sales_order_row_id: int):
    return db.query(row_model.SalesOrderRow).filter(row_model.SalesOrderRow.sales_order_row_id==sales_order_row_id).first()


# create order_row
def create_order_row(db: Session, order_row: row_schema.CreateSalesOrderRow):
    new_row = row_model.SalesOrderRow(
        sales_order_id=order_row.sales_order_id,
        quantity=order_row.quantity,
        variant_id=order_row.variant_id,
        tax_rate_id=order_row.tax_rate_id,
        price_per_unit=order_row.price_per_unit,

        created_at=datetime.now()
        )
    db.add(new_row)
    db.commit()
    return new_row

#update order_row info
def update_order_row(db: Session, order_row: row_schema. UpdateSalesOrderRow):
    row_data = db.query(row_model.SalesOrderRow).filter(row_model.SalesOrderRow.sales_order_row_id == order_row.sales_order_row_id).first()
    row_data.sales_order_id=order_row.sales_order_id,
    row_data.quantity=order_row.quantity,
    row_data.variant_id=order_row.variant_id,
    row_data.tax_rate_id=order_row.tax_rate_id,
    row_data.price_per_unit=order_row.price_per_unit,

    row_data.updated_at==datetime.now()
    db.commit()
    db.refresh(row_data)
    return row_data

#delete order_row
def delete_order_row(db: Session, order_row: row_schema.DeleteSalesOrderRow):
    row_data = db.query(row_model.SalesOrderRow).filter(row_model.SalesOrderRow.sales_order_row_id == order_row.sales_order_row_id).first()
    print(row_data)
    if not row_data:
        return None
    else:
        db.delete(row_data)
        db.commit()
        return row_data