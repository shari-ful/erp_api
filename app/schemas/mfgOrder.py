from pydantic import BaseModel


class CreateMfgOrder(BaseModel):
    status: str | None = None
    order_no: str
    variant_id: int
    location_id: str
    planned_quantity: int | None = None
    actual_quantity: int | None = None
    order_created_date: str | None = None
    production_deadline_date: str | None = None
    additional_info: str | None = None
    batch_transactions: dict | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "status": "steel",
                "order_no": "billing",
                "variant_id": 2,
                "location_id": 1,
                "planned_quantity": 25,
                "actual_quantity": 81,
                "order_created_date": "12 july, 2022",
                "production_deadline_date": "12 july, 2022",
                "additional_info": "mfg order"
            }
        }

class UpdateMfgOrder(BaseModel):
    mfg_order_id: int
    status: str | None = None
    order_no: str | None = None
    variant_id: int | None = None
    location_id: str | None = None
    planned_quantity: int | None = None
    actual_quantity: int | None = None
    order_created_date: str | None = None
    production_deadline_date: str | None = None
    additional_info: str | None = None
    batch_transactions: dict | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "mfg_order_id": 5,
                "status": "steel",
                "order_no": "billing",
                "variant_id": 2,
                "location_id": 1,
                "planned_quantity": 25,
                "actual_quantity": 81,
                "order_created_date": "12 july, 2022",
                "production_deadline_date": "12 july, 2022",
                "additional_info": "mfg order"
            }
        }

class DeleteMfgOrder(BaseModel):
    mfg_order_id: int
    
    class Config:
        orm_mode = True
        schema_extra = {
            "mfg_order_id": 11
        }



