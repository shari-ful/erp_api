from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...config.dbpostgres import get_db, engine
from ...schemas import users as users_schema
from ...models import users as users_model
from ..crud.users import *

users_model.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/user", tags=['users'])
async def create_user(user: users_schema.CreateUser, db: Session = Depends(get_db)):
    return create_users(user=user, db=db)