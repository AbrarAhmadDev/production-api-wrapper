from sqlalchemy import Column,Integer,String,DateTime

from datetime import datetime

from app.database.base import Base


class Usage(Base):

    __tablename__="usage"


    id=Column(
        Integer,
        primary_key=True
    )


    user_id=Column(
        Integer
    )


    endpoint=Column(
        String
    )


    created_at=Column(
        DateTime,
        default=datetime.utcnow
    )