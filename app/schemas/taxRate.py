from pydantic import BaseModel


class CreateTaxRate(BaseModel):
    name: str | None = None 
    rate: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "foreign tax",
                "rate": 52
            }
        }

class UpdateTaxRate(BaseModel):
    tax_rate_id: int
    name: str | None = None 
    rate: int | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "tax_rate_id": 2,
                "name": "foreign tax",
                "rate": 52
            }
        }

class DeleteTaxRate(BaseModel):
    tax_rate_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "tax_rate_id": 11
        }

