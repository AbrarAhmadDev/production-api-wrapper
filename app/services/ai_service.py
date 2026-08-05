from app.clients.gemini_client import GeminiClient


async def generate_text(prompt:str):

    client = GeminiClient()


    result = await client.generate(prompt)


    return result