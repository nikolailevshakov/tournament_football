import requests
import sys
sys.path.append('../bot')
import envs
import utils


def send_to_telegram(message):
    chatID = '-1001809163992'
    apiURL = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'

    try:
        requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)


post_message = "Четвертая неделя!\n" + utils.read_games()
send_to_telegram(post_message)
