from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database.base import Base


class APIKey(Base):

    __tablename__="api_keys"


    id = Column(
        Integer,
        primary_key=True
    )


    key = Column(
        String,
        unique=True,
        nullable=False
    )


    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )