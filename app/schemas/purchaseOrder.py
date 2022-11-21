from pydantic import BaseModel


class CreatePurchaseOrder(BaseModel):
    order_no: str
    entity_type: str | None = None
    status: str | None = None
    supplier_id: int
    location_id: int
    currency: str | None = None
    expected_arrival_date: str | None = None
    order_created_date: str | None = None
    tracking_location_id: str | None = None
    additional_info: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "order_no": "fergtr",
                "entity_type": "billing",
                "status": "active",
                "supplier_id": 125,
                "location_id": 521,
                "currency": "usd",
                "expected_arrival_date": "21 july, 2022",
                "order_created_date": "21 july, 2022",
                "tracking_location_id": "BDT",
                "additional_info": "purchased order"
            }
        }


class UpdatePurchaseOrder(BaseModel):
    order_id: int
    order_no: str | None = None
    entity_type: str | None = None
    status: str | None = None
    supplier_id: int | None = None
    location_id: int | None = None
    currency: str | None = None
    expected_arrival_date: str | None = None
    order_created_date: str | None = None
    tracking_location_id: str | None = None
    additional_info: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "order_no": 2,
                "order_no": "fergtr",
                "entity_type": "billing",
                "status": "active",
                "supplier_id": 125,
                "location_id": 521,
                "currency": "usd",
                "expected_arrival_date": "21 july, 2022",
                "order_created_date": "21 july, 2022",
                "tracking_location_id": "BDT",
                "additional_info": "purchased order"
            }
        }

class DeletePurchaseOrder(BaseModel):
    order_id: int

    class Config:
        orm_mode = True

class ResponseData(BaseModel):
    quantity: int | None = None
    variant_id: int | None = None
    tax_rate_id: int | None = None
    price_per_unit: float | None = None
    price_per_unit_in_base_currency: float | None = None
    purchase_uom_conversion_rate: float | None = None
    purchase_uom: str | None = None
    total: int | None = None  
    created_at: str | None = None
    updated_at: str | None = None
    deleted_at: str | None = None
    currency: str | None = None
    conversion_rate: float | None = None
    conversion_date: str | None = None
    received_date: str | None = None
    purchase_order_id: int | None = None


class GetPurchaseOrderResponse(BaseModel):
    data: list[ResponseData] = []


    