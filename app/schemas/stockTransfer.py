from pydantic import BaseModel

class CreateStockTransfer(BaseModel):
    stock_transfer_number: str
    source_location_id: int
    target_location_id: int
    transfer_date: str | None = None
    additional_info: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stock_transfer_number": "S-21",
                "source_location_id": 2,
                "target_location_id": 5,
                "transfer_date": "fdsf",
                "additional_info": "fddrftd"
            }
        }

class UpdateStockTransfer(BaseModel):
    stock_transfer_id: int
    stock_transfer_number: str | None = None
    transfer_date: str | None = None
    additional_info: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stock_transfer_id": 5,
                "stock_transfer_number": "S-21",
                "transfer_date": "fdsf",
                "additional_info": "fddrftd"
            }
        }

class DeleteStockTransfer(BaseModel):
    stock_transfer_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stock_transfer_id": 5
            }
        }
