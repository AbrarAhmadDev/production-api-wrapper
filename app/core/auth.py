from fastapi import Depends, HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from sqlalchemy.orm import Session

from app.core.config import settings

from app.database.dependency import get_db

from app.repositories.user_repository import get_user_by_email


oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login"

)


def get_current_user(

    token:str = Depends(oauth2_scheme),

    db:Session = Depends(get_db)

):

    payload = jwt.decode(

        token,

        settings.JWT_SECRET,

        algorithms=[
            settings.JWT_ALGORITHM
        ]

    )


    email = payload.get("email")


    user = get_user_by_email(
        db,
        email
    )


    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )


    return user