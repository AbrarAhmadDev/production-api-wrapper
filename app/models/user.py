from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.base import Base


class User(Base):

    __tablename__="users"


    id = Column(
        Integer,
        primary_key=True
    )


    email = Column(
        String,
        unique=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )