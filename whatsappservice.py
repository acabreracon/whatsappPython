import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAJFZBZCbrYkoBO8GLe4jYwiwIBJFZCIyuf9kX53gdnKUWyIp0tI1sAi1WfZBaQsDdSyS1EBpBiizPkf3AiUaUNWDojLzswfZA6cByggnzmsnbZBfw7ykZB4tQU9gxUfp9PqSKcMn9YZBlsWd4JHZC9AcZAWRjYKZAOV3A9GzfI73qWAKfYM4yKaltooVBPm8fRmgZDZD"
        api_url = "https://graph.facebook.com/v21.0/566794819850915/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False