from datetime import datetime, timedelta, timezone

from jose import jwt

from app.core.config import settings

from datetime import timedelta



def create_access_token(
    data: dict
):

    to_encode = data.copy()


    expire = datetime.now(timezone.utc) + timedelta(

        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES

    )


    to_encode.update(
        {
            "exp": expire
        }
    )


    return jwt.encode(

        to_encode,

        settings.JWT_SECRET,

        algorithm=settings.JWT_ALGORITHM

    )


def create_refresh_token(
    data:dict
):

    expire = datetime.now(timezone.utc) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )


    data.update(
        {
            "exp":expire,
            "type":"refresh"
        }
    )


    return jwt.encode(
        data,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM
    )