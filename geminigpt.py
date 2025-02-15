from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

def GetResponse(text):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text,
        )
        return response.text

    except Exception as exception:
        print(exception)
        return "error"