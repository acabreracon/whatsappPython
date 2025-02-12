def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print ("sin mensaje")
    else:
        print ("sin mensaje")
    
    return text

def TextMessage(text, number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "text":{
                    "body": text
                },
                "type": "text"
            }
    return data

def TextFormatMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "body": "*Hola usuario* - _Hola usuario_ - ~Hola usuario~ - `Hola usuario`"
            }
            }
    return data

def ImageMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "image",
            "image": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/image_whatsapp.png"
            }
            }
    return data

def AudioMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "audio",
            "audio": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"
            }
            }
    return data

def VideoMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "video",
            "video": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"
            }
            }
    return data

def DocumentMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "document",
            "document": {
                "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf"
            }
            }
    return data

def LocationMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "location",
                "location": {
                    "latitude":"21.17196358517015",
                    "longitude":"-86.85827065100767",
                    "name":"Bodega Aurrera",
                    "address":"Calle Prol. Av. Kabáh s/n, 77516 Cancún, Q.R."

                }
            }
    return data

def ButtonsMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "¿Tiene una cuenta?"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "iniciar sesión 😁"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "Registrarse"
                                }
                            }
                        ]
                    }
                }
            }
    return data

def ListMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "✅ I have these options"
                    },
                    "footer": {
                        "text": "Select an option"
                    },
                    "action": {
                        "button": "See options",
                        "sections": [
                            {
                                "title": "Buy and sell products",
                                "rows": [
                                    {
                                        "id": "main-buy",
                                        "title": "Buy",
                                        "description": "Buy the best product your home"
                                    },
                                    {
                                        "id": "main-sell",
                                        "title": "Sell",
                                        "description": "Sell your products"
                                    }
                                ]
                            },
                            {
                                "title": "📍center of attention",
                                "rows": [
                                    {
                                        "id": "main-agency",
                                        "title": "Agency",
                                        "description": "Your can visit our agency"
                                    },
                                    {
                                        "id": "main-contact",
                                        "title": "Contact center",
                                        "description": "One of our agents will assist you"
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
    return data




