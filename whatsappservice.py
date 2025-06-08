import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAJFZBZCbrYkoBO0sJWBSqAJQv8Wc8eexKpBEZCQxnwYu1kUDcDVAplVdE0XhcJsZClfQmSJe4ANWweb4ZCAnDQ3SZBASBmww5unUwcb4rOTVAudIAfNS0jDMxbwMqB9iwcR5ZBG9yadZClWnrvvdpLdw0yoW4bookkRcMoAFHAgDwknExq8jBNaRgPaejdCGBWBngZDZD"
        api_url = "https://graph.facebook.com/v21.0/566794819850915/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False