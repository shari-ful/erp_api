from pydantic import BaseModel, Field


class CreateBatch(BaseModel):   
    batch_number: str
    expiration_date: str | None = None
    batch_created_date: str | None = None
    variant_id: int 
    batch_barcode: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "batch_number": "B-24",
                "expiration_date": "12 july 2024",
                "batch_created_date": "12 july 2022",
                "variant_id": 5,
                "batch_barcode": "b24c41"
            }
        }


class UpdateBatch(BaseModel):
    batch_number: str | None = None
    expiration_date: str | None = None
    batch_created_date: str | None = None
    variant_id: int | None = None
    batch_barcode: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "batch_number": "B-24",
                "expiration_date": "12 july 2024",
                "batch_created_date": "12 july 2022",
                "variant_id": 5,
                "batch_barcode": "b24c41"
            }
        }

class DeleteBatch(BaseModel):
    class Config:
        orm_mode = True




    

