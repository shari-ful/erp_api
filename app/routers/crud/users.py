from sqlalchemy.orm import Session
from ...models import users as users_model
from ...schemas import users as users_schema


def create_users(db: Session, user: users_schema.CreateUser):
    new_user = users_model.User(
        username=user.username,
        full_name=user.full_name,
        email=user.email
        )
    db.add(new_user)
    db.commit()
    return new_user
