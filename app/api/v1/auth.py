from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.dependency import get_db

from app.schemas.user import UserLogin

from app.services.auth_service import login_user

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services.user_service import register_user


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(

    user:UserCreate,

    db:Session = Depends(get_db)

):

    return register_user(
        db,
        user.email,
        user.password
    )

@router.post("/login")
def login(

    user:UserLogin,

    db:Session = Depends(get_db)

):

    token = login_user(

        db,

        user.email,

        user.password

    )


    return {

        "access_token":token,

        "token_type":"bearer"

    }