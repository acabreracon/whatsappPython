from flask import Flask, request
import util
import whatsappservice
import re
import chatgptservice
import geminigpt

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def index():
    return "Welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        accessToken = "fsdfasdfasdfasdfasdfasdfasdf"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400
    
@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        number = LimpiarNumero(number)

        text = util.GetTextUser(message)
        responseGPT = geminigpt.GetResponse(text)#chatgptservice.GetResponse(text)

        if responseGPT != "error":
            data = util.TextMessage(responseGPT, number)
        else:
            data = util.TextMessage("Lo siento, ocurrio un problema", number)

        whatsappservice.SendMessageWhatsapp(data)
        #ProccessMessage(text, number)

        return "EVENT_RECEIVED" #Si no se devuelve este mensaje, las APIS de WA, pensarán que aún no he recibido el mensaje, Se hace un bucle
    except:
        return "EVENT_RECEIVED"
    
def ProccessMessage(text, number):
    text = text.lower()
    listData = []
    
    if "hi" in text or "option" in text:
        data = util.TextMessage("Hello, how i can help you", number)
        dataMenu = util.ListMessage(number)

        listData.append(data)
        listData.append(dataMenu)

    elif "thanks" in text:
        data = util.TextMessage("Thank you for contacting me", number)

    elif "agency" in text:
        data = util.TextMessage("This is our agency", number)
        dataLocation = util.LocationMessage(number)
        listData.append(data)
        listData.append(dataLocation)

    elif "contact" in text:
        data = util.TextMessage("*Contact center:*\n9983467026", number)
        listData.append(data)

    elif "buy" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)

    elif "sell" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)
    
    elif "sign up" in text or "signup" in text:
        data = util.TextMessage("Enter this link to sign up: https://google.com.mx", number)
        listData.append(data)
    
    elif "login" in text or "log in" in text:
        data = util.TextMessage("Enter this link to sign up: https://google.com.mx", number)
        listData.append(data)
        
    else:
        data = util.TextMessage("Sorry, i can't understand you, but this is our menu", number)
        listData.append(data)
        dataMenu = util.ListMessage(number)
    
    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)

def GenerateMessage(text, number):

    text = text.lower()
    if "text" in text:
        data = util.TextMessage("Text", number)
    
    if "format" in text:
        data = util.TextFormatMessage(number)
    
    if "image" in text:
        data = util.ImageMessage(number)
    
    if "video" in text:
        data = util.VideoMessage(number)

    if "audio" in text:
        data = util.AudioMessage(number)

    if "document" in text:
        data = util.DocumentMessage(number)

    if "location" in text:
        data = util.LocationMessage(number)

    if "buttons" in text:
        data = util.ButtonsMessage(number)

    if "list" in text:
        data = util.ListMessage(number)

    whatsappservice.SendMessageWhatsapp(data)

def LimpiarNumero(numero):
    return re.sub(r"^521(\d{10})$", r"52\1", numero)


if (__name__ == "__main__"):
    app.run()