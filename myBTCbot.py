from bs4 import BeautifulSoup  #del modulo bs4 we need this
import requests
import schedule

def bot_send_text(bot_message):
    bot_token = 'myToken'
    bot_chatID = 'myChatID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response

test_bot = bot_send_text('Hello World!')