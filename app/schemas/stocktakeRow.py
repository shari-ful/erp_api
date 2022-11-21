from pydantic import BaseModel

class CreateStocktakeRow(BaseModel):
    stocktake_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_id": 1
            }
        }

class UpdateStocktakeRow(BaseModel):
    stocktake_row_id: int
    variant_id: int | None = None
    batch_id: int | None = None
    notes: str | None = None
    counted_quantity: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_row_id": 1,
                "variant_id": 2,
                "batch_id": 5,
                "notes": "fdsf",
                "counted_quantity": 4
            }
        }

class DeleteStocktakeRow(BaseModel):
    stocktake_row_id: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_row_id": 1
            }
        }
