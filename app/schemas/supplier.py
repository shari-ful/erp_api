from pydantic import BaseModel


class CreateSupplier(BaseModel):
    name: str
    currency: str | None = None
    email: str | None = None
    comment: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "fergtr",
                "currency": "usd",
                "email": "fergtr@gmail.com",
                "comment": "new supplier"
            }
        }


class UpdateSupplier(BaseModel):
    supplier_id: int
    name: str | None = None
    currency: str | None = None
    email: str | None = None
    comment: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "supplier_id": 2,
                "name": "fergtr",
                "currency": "usd",
                "email": "fergtr@gmail.com",
                "comment": "new supplier"
            }
        }

class DeleteSupplier(BaseModel):
    supplier_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "supplier_id": 2
            }
        }


  