from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)

from app.models.user import User

from app.core.password import hash_password



def register_user(
    db:Session,
    email:str,
    password:str
):

    existing = get_user_by_email(
        db,
        email
    )


    if existing:

        raise Exception(
            "User already exists"
        )


    user = User(

        email=email,

        hashed_password=
        hash_password(password)

    )


    return create_user(
        db,
        user
    )