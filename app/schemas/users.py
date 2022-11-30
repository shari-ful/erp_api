from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "jdim",
                "email": "jdim@erp.com",
                "full_name": "Jhon Dim",
                "disabled": True
            }
        }