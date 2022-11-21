from pydantic import BaseModel

class CreateLocation(BaseModel):
    name: str | None = None
    legal_name: str | None = None 
    address_id: int | None = None
    is_primary: bool | None = None
    sales_allowed: bool | None = None
    manufacturing_allowed: bool | None = None
    purchase_allowed: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "gfygrv",
                "legal_name": "dsfdsf",
                "address_id": 2,
                "is_primary": False,
                "sales_allowed": False,
                "manufacturing_allowed": False,
                "purchase_allowed": False
            }
        }


class UpdateLocation(BaseModel):
    location_id: int
    name: str | None = None
    legal_name: str | None = None 
    address_id: int | None = None
    is_primary: bool | None = None
    sales_allowed: bool | None = None
    manufacturing_allowed: bool | None = None
    purchase_allowed: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "gfygrv",
                "legal_name": "dsfdsf",
                "address_id": 2,
                "is_primary": False,
                "sales_allowed": False,
                "manufacturing_allowed": False,
                "purchase_allowed": False
            }
        }

class DeleteLocation(BaseModel):
    location_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "location_id": 11
        }

class LocationResponse(BaseModel):
    data: list[CreateLocation] | None = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "location_id": 4545,
                "variant_id": 741,
                "value": 748
            }
        }