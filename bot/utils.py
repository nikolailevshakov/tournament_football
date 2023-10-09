import codecs
import os
from translate import Translator
import requests
from tabulate import tabulate
import json


def read_games():
    file = codecs.open("./files/games.txt", "r", "utf-8-sig")
    lines = file.readlines()
    lines = [line.replace('-', '🆚') for line in lines]
    return "".join(lines)


def clear_games():
    open('./files/games.txt', 'w').close()


def if_games_empty():
    return os.path.getsize("./files/games.txt") == 0


def talk_response():
    api_url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
    insult = requests.get(api_url).json()["insult"]
    translator = Translator(to_lang="ru")
    return translator.translate(insult)


def organize_results(all_texts):
    all_texts.sort(reverse = True, key=lambda x: x[2])
    all_texts[0][0] = "🥇" + all_texts[0][0]
    all_texts[1][0] = "🥈" + all_texts[1][0]
    all_texts[2][0] = "🥉" + all_texts[2][0]
    all_texts[3][0] = "😒" + all_texts[3][0]
    all_texts[4][0] = "🤡" + all_texts[4][0]
    df = tabulate(all_texts, headers=["Участник", "Неделя", "Сезон"], tablefmt="github")
    return df
