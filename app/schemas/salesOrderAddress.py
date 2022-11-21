from pydantic import BaseModel


class CreateSalesAddress(BaseModel):  
    sales_order_id: int
    entity_type: str
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    phone: str | None = None
    line_1: str | None = None
    line_2: str | None = None
    city: str | None = None
    state: str | None = None
    zip: str | None = None
    country: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_id": 3215,
                "entity_type": "billing",
                "first_name": "John",
                "last_name": "Bell",
                "company": "Intellier",
                "phone": "+8801234567890",
                "line_1": "Uttara sector #3",
                "line_2": "jasimuddin Avenue",
                "city": "Dhaka",
                "state": "Dhaka",
                "zip": "1230",
                "country": "Bangladesh"              
            }
        }

class UpdateSalesAddress(BaseModel):
    address_id: int
    sales_order_id: int | None = None
    entity_type: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    phone: str | None = None
    line_1: str | None = None
    line_2: str | None = None
    city: str | None = None
    state: str | None = None
    zip: str | None = None
    country: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "sales_order_id": 3215,
                "entity_type": "billing",
                "first_name": "John",
                "last_name": "Bell",
                "company": "Intellier",
                "phone": "+8801234567890",
                "line_1": "Uttara sector #3",
                "line_2": "jasimuddin Avenue",
                "city": "Dhaka",
                "state": "Dhaka",
                "zip": "1230",
                "country": "Bangladesh"            
            }
        }


class DeleteSalesAddress(BaseModel):
    address_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "address_id": 11
        }

        