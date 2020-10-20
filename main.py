from telegrambot import TelegramBot
import time
import requests 

def main():
    rasa_server = "http://127.0.0.1:5005/webhooks/rest/webhook"
    bot = TelegramBot("1387499885:AAGiqlocFqKvldZtOptrltLbdOWHIAHNlVA")
    res = bot.get_me()
    #name = res["result"]["first_name"]
    print(res)
    print("Bot Ready...")
    while True:
        messages = bot.get_update()
        if messages:
            for msg in messages:
                print(msg.message)
                print(msg.chat_id)
                print(msg.user)
                res = requests.post(rasa_server, json={"message": msg.message, "sender":msg.chat_id}).json()
                print(res)
                if(res):
                    print(res[0]["text"])
                    bot.send_message(f"{res[0]['text']}", msg.chat_id)
                print("=="*5 + "**" + "=="*5)
            print(" - - - - - - -")
            print("")
            print("- -")
        time.sleep(1)

main()