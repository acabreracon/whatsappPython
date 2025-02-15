from google import genai

client = genai.Client(api_key="AIzaSyCrulqkz40W9JLpowAP2xC-yXqu6fg5zT8")

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