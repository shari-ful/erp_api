from pydantic import BaseModel


class BaseOrderRow(BaseModel):
    order_row_id: int

class CreateOrderRow(BaseOrderRow):
    quantity: int