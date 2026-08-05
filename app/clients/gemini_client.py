import httpx

from app.core.config import settings
from fastapi import HTTPException

class GeminiClient:


    def __init__(self):

        self.api_key = settings.GEMINI_API_KEY

        self.base_url = (
            "https://generativelanguage.googleapis.com"
        )


    async def generate(
        self,
        prompt:str
    ):


        url = (
            f"{self.base_url}/v1/models/"
            f"gemini-pro:generateContent"
        )


        headers = {
            "Content-Type":"application/json"
        }


        payload = {

            "contents":[

                {
                    "parts":[
                        {
                            "text":prompt
                        }
                    ]
                }

            ]

        }


        async with httpx.AsyncClient() as client:

            response = await client.post(

                url,

                headers=headers,

                json=payload,

                timeout = httpx.Timeout(
                    connect=5,
                    read=30,
                    write=10,
                    pool=5
                )

            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=502,
                    detail="AI provider unavailable"
                )


        return response.json()