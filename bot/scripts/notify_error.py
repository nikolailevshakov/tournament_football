import requests
import sys
sys.path.append('../bot')
import envs


def send_to_telegram(message):
    chatID = '212288934'
    apiURL = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'

    try:
        requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e:
        print(e)

