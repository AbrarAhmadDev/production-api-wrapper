from sqlalchemy.orm import Session

from app.repositories.user_repository import (
    get_user_by_email
)

from app.core.password import (
    verify_password
)

from app.core.jwt import (
    create_access_token
)


def login_user(
    db:Session,
    email:str,
    password:str
):

    user = get_user_by_email(
        db,
        email
    )


    if not user:

        raise Exception(
            "Invalid credentials"
        )


    if not verify_password(
        password,
        user.hashed_password
    ):

        raise Exception(
            "Invalid credentials"
        )


    token = create_access_token(
        {
            "user_id":user.id,
            "email":user.email
        }
    )


    return token