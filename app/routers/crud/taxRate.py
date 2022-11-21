from sqlalchemy.orm import Session
from ...models import taxRate as tax_rate_model
from ...schemas import taxRate as tax_rate_schema


#get tax_rate
def get_tax_rate(db: Session, skip: int = 0, limit: int = 50):
    return db.query(tax_rate_model.TaxRate).offset(skip).limit(limit).all()

def get_tax_rate_by_id(db: Session, tax_rate_id: int):
    return db.query(tax_rate_model.TaxRate).filter(tax_rate_model.TaxRate.tax_rate_id==tax_rate_id).first()


# create tax_rate
def create_tax_rate(db: Session, tax_rate: tax_rate_schema.CreateTaxRate):
    new_tax_rate = tax_rate_model.TaxRate(
        name=tax_rate.name,
        rate=tax_rate.rate   
        )
    db.add(new_tax_rate)
    db.commit()
    return new_tax_rate

