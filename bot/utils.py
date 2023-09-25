import codecs
import os
from translate import Translator
import requests
import pandas as pd


def read_games():
    file = codecs.open("./files/games.txt", "r", "utf-8-sig")
    lines = file.readlines()
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
    df = pd.DataFrame(columns=["Участник", "Неделя", "Сезон"])
    for line in all_texts:
        df.loc[len(df)] = line
    df.sort_values(by=["Сезон", "Неделя"], ascending=False, inplace=True)
    return df
