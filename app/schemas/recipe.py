from pydantic import BaseModel


class CreateRecipe(BaseModel):
    name: str
    currency: str | None = None
    email: str | None = None
    comment: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "fergtr",
                "currency": "usd",
                "email": "fergtr@gmail.com",
                "comment": "new recipe"
            }
        }


class UpdateRecipe(BaseModel):
    recipe_id: int
    name: str | None = None
    currency: str | None = None
    email: str | None = None
    comment: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "recipe_id": 2,
                "name": "fergtr",
                "currency": "usd",
                "email": "fergtr@gmail.com",
                "comment": "new recipe"
            }
        }

class DeleteRecipe(BaseModel):
    recipe_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "recipe_id": 2
            }
        }

  