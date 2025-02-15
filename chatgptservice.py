import openai

client = openai.Client(api_key = "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")

def GetResponse(text):
    try:
        #openai.api_key = "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"
        # result = openai.Completion.create(model = "text-davinci-003", 
        #                                    prompt=text,
        #                                    n = 1,
        #                                    max_tokens= 500)
        print(text)

        result = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": text}
            ]
        )
        
        response = result.choices[0].message.content
        return response
    except openai.OpenAIError as e:
        print(f"Error en la API de OpenAI: {e}")
        return "Error en la API"

    except Exception as e:
        print(f"Error inesperado: {e}")
        return "Error desconocido"