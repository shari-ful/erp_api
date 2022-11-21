from pydantic import BaseModel


class CreateInventory(BaseModel):
    location_id: int 
    variant_id: int
    value: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "location_id": 4545,
                "variant_id": 741,
                "value": 748
            }
        }


class UpdateInventory(BaseModel):
    inventory_id: int
    location_id: int | None = None
    variant_id: int | None = None
    value: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "inventory_id": 2,
                "location_id": 4545,
                "variant_id": 741,
                "value": 748
            }
        }


class DeleteInventory(BaseModel):
    inventory_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "inventory_id": 11
        }

