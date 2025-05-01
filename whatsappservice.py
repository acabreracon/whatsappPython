import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAJFZBZCbrYkoBOzSQdSyMd3q6yJzCyHB61Po7Lw7Ao3RhTzKhYgH4FsDp5wMAGxmZBi4ln9QXFZCR8LtBi4S6gA3qYbVonCCs1ZALpIrT3ixYeSZA3TYfpgGBEWAnPsQsi4j43EfGEJJBZCSDJPq4FxB3URTK7PsDVMvyJZCLUBu92filLURwwa6nb9xfhOml1EeYyMwkpSStgZAVXBdRpq4QRpHcYKBNJDSRIqJZB5GI"
        api_url = "https://graph.facebook.com/v21.0/566794819850915/messages"
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:
            return True
        
        return False
    
    except Exception as exception:
        print(exception)
        return False