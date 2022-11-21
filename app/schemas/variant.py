from pydantic import BaseModel, Field
 

class CreateVariant(BaseModel):   
    sku: str | None = None
    sales_price: int | None = None
    purchase_price: int | None = None
    product_id: int 
    internal_barcode: str | None = None
    registered_barcode: str | None = None
    material_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sku": "B-24",
                "sales_price": 12,
                "purchase_price": 10,
                "product_id": 1,
                "internal_barcode": "b24c41",
                "registered_barcode": "b24c41",
                "material_id": 2
            }
        }


class UpdateVariant(BaseModel):
    variant_id: int
    sku: str | None = None
    sales_price: int | None = None
    purchase_price: int | None = None
    product_id: int | None = None
    internal_barcode: str | None = None
    registered_barcode: str | None = None
    material_id: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "variant_id": 1,
                "sku": "B-24",
                "sales_price": 12,
                "purchase_price": 10,
                "product_id": 1,
                "internal_barcode": "b24c41",
                "registered_barcode": "b24c41",
                "material_id": 2
            }
        }

class DeleteVariant(BaseModel):
    variant_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "variant_id": 1
            }
        }

class GetResponseVariant(BaseModel):
    variant_id: int
    variant_number: str
    variant_created_date: str
    expiration_date: str
    location_id: int
    variant_id: int
    quantity_in_stock: int
    variant_barcode: str

    

