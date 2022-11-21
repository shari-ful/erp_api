from pydantic import BaseModel

class CreateStocktake(BaseModel):
    stocktake_number: str
    location_id: int 
    reason: str | None = None
    additional_info: str | None = None
    created_date: str | None = None
    set_remaining_items_as_counted: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_number": "S-54",
                "location_id": 4,
                "reason": "wefdewf",
                "additional_info": "egfrgg",
                "created_date": "14 july 2022",
                "set_remaining_items_as_counted": False
            }
        }

class UpdateStocktake(BaseModel):
    stocktake_number: str | None = None
    location_id: int | None = None
    status: str | None = None
    reason: str | None = None
    additional_info: str | None = None
    created_date: str | None = None
    completed_date: str | None = None
    set_remaining_items_as_counted: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_number": "S-54",
                "location_id": 4,
                "status": "active",
                "reason": "wefdewf",
                "additional_info": "egfrgg",
                "created_date": "14 july 2022",
                "completed_date": "14 july 2022",
                "set_remaining_items_as_counted": False
            }
        }

class DeleteStocktake(BaseModel):
    stocktake_id: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "stocktake_id": 1
            }
        }
