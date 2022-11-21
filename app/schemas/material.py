from pydantic import BaseModel
  

class CreateMaterial(BaseModel):
    name: str
    uom: str | None = None
    category_name: str | None = None
    default_supplier_id: str | None = None
    type: str | None = None
    additional_info: str | None = None
    purchase_uom: str | None = None
    purchase_uom_conversion_rate: int | None = None
    batch_tracked: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "steel",
                "uom": "billing",
                "category_name": "category 1",
                "default_supplier_id": 2541,
                "type": "frehff",
                "additional_info": "product",
                "purchase_uom": "gfgdfh",
                "purchase_uom_conversion_rate": 84,
                "batch_tracked": False
            }
        }

class UpdateMaterial(BaseModel):
    material_id: int
    name: str | None = None
    uom: str | None = None
    category_name: str | None = None
    default_supplier_id: str | None = None
    type: str | None = None
    additional_info: str | None = None
    purchase_uom: str | None = None
    purchase_uom_conversion_rate: int | None = None
    batch_tracked: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "material_id": 1,
                "name": "steel",
                "uom": "billing",
                "category_name": "category 1",
                "default_supplier_id": 2541,
                "type": "frehff",
                "additional_info": "product",
                "purchase_uom": "gfgdfh",
                "purchase_uom_conversion_rate": 21,
                "batch_tracked": False
            }
        }

class DeleteMaterial(BaseModel):
    material_id: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "material_id": 11
        }



