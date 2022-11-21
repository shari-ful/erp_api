from pydantic import BaseModel


class CreateSalesOrderRow(BaseModel):
    sales_order_id: int
    quantity: int
    variant_id: int
    tax_rate_id: int | None = None
    price_per_unit: int | None = None


    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_id": 1,
                "quantity": 5,
                "variant_id": 2,
                "tax_rate_id": 4,
                "price_per_unit": 42.5
            }
        }

class UpdateSalesOrderRow(BaseModel):
    sales_order_row_id: int
    sales_order_id: int | None = None
    quantity: int | None = None
    variant_id: int | None = None
    tax_rate_id: int | None = None
    price_per_unit: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_row_id": 1,
                "sales_order_id": 4,
                "quantity": 5,
                "variant_id": 2,
                "tax_rate_id": 4,
                "price_per_unit": 42.5
            }
        }
class DeleteSalesOrderRow(BaseModel):
    sales_order_row_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_row_id": 1
            }
        }
