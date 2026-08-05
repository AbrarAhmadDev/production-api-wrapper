from fastapi import HTTPException

from app.database.redis import redis_client



def check_rate_limit(
    api_key:str
):

    key=f"rate:{api_key}"


    requests = redis_client.incr(key)


    if requests == 1:

        redis_client.expire(
            key,
            3600
        )


    if requests > 100:

        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )