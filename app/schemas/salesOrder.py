from pydantic import BaseModel


class CreateSalesOrder(BaseModel):
    order_no: str
    customer_id: int
    tracking_number: str | None = None
    tracking_number_url: str | None = None
    order_created_date: str | None = None
    delivery_date: str | None = None
    currency: str | None = None
    location_id: int | None = None
    status: str | None = None
    additional_info: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "order_no": "854",
                "customer_id": "2154",
                "tracking_number": "451",
                "tracking_number_url": "gfyy.com",
                "order_created_date": "12 july 2022",
                "delivery_date": "12 july 2022",
                "currency": "EUR",
                "location_id": 514,
                "status": "active",
                "additional_info": "ew4t4et5t"
            }
        }


class UpdateSalesOrder(BaseModel):
    sales_order_id: int
    order_no: str | None = None
    customer_id: str | None = None
    order_created_date: str | None = None
    delivery_date: str | None = None
    picked_date: str | None = None
    location_id: int | None = None
    status: str | None = None
    currency: str | None = None
    conversion_rate: int | None = None
    conversion_date: str | None = None
    additional_info: str | None = None
    tracking_number: str | None = None
    tracking_number_url: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_id": 2,
                "order_no": "854",
                "customer_id": "2154",
                "order_created_date": "12 july 2022",
                "delivery_date": "12 july 2022",
                "picked_date": "12 july 2022",
                "location_id": 514,
                "status": "active",
                "currency": "EUR",                
                "additional_info": "ew4t4et5t",
                "tracking_number": "451",
                "tracking_number_url": "gfyy.com"
            }
        }

class DeleteSalesOrder(BaseModel):
    sales_order_id: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_id": 2
            }
        }

  