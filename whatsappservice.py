import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAJFZBZCbrYkoBO6Ff5rpmTNu1rjZAWyQ3pkolH1i6KCqpgx16P5xA9d4p1iOQdpGSYjFUxPgmv6kKBAB6J7nRvNoBnZBTxvVhAFvu6FhiJFeoBfsEdp7DN8bwxlkZAswuow5z7foZAcZAlSeZAKLG0d4VvP6YBIK1FYZCcFiJBxMUWNhIoeQ1bWxVXuXHkY0nQwAnwZDZD"
        api_url = "https://graph.facebook.com/v21.0/566794819850915/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False