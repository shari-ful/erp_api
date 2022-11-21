from pydantic import BaseModel

class CreateWebhook(BaseModel):
    url: str
    description: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "url": "sdsff.com",
                "description": "w3e3wr4ert"
            }
        }

class UpdateWebhook(BaseModel):
    webhook_id: int
    url: str | None = None
    enabled: bool | None = None
    description: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "webhook_id": 2,
                "url": "sdsff.com",
                "enabled": True,
                "description": "w3e3wr4ert"
            }
        }

class DeleteWebhook(BaseModel):
    webhook_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "webhook_id": 2
            }
        }

