from pydantic import BaseModel

class CreateProduct(BaseModel):
    uom: str | None = None
    name: str | None = None
    category_name: str | None = None 
    is_producible: bool | None = None
    is_purchasable: bool | None = None
    default_supplier_id: int | None = None
    additional_info: str | None = None
    batch_tracked: bool | None = None
    purchase_uom: str | None = None
    purchase_uom_conversion_rate: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "uom": "billing",
                "name": "gfygrv",
                "category_name": "category 1",
                "is_producible": False,
                "is_purchasable": False,
                "default_supplier_id": 2541,
                "additional_info": "product",
                "batch_tracked": False,
                "purchase_uom": "hgtrg",
                "purchase_uom_conversion_rate": 12
            }
        }


class UpdateProduct(BaseModel):
    product_id: int
    uom: str | None = None
    name: str | None = None
    category_name: str | None = None 
    is_producible: bool | None = None
    is_purchasable: bool | None = None
    default_supplier_id: int | None = None
    additional_info: str | None = None
    batch_tracked: bool | None = None
    purchase_uom: str | None = None
    purchase_uom_conversion_rate: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "product_id": 1,
                "uom": "billing",
                "name": "gfygrv",
                "category_name": "category 1",
                "is_producible": False,
                "is_purchasable": False,
                "default_supplier_id": 2541,
                "additional_info": "product",
                "batch_tracked": False,
                "purchase_uom": "hgtrg",
                "purchase_uom_conversion_rate": 14
            }
        }

class DeleteProduct(BaseModel):
    product_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "product_id": 11
        }

class ProductResponse(BaseModel):
    data: list[CreateProduct] | None = None
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "location_id": 4545,
                "variant_id": 741,
                "value": 748
            }
        }