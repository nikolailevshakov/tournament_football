import codecs
import os
from translate import Translator
import requests
from tabulate import tabulate
import chatgpt
import random


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


def interest_fact_team():
    file = codecs.open("./files/games.txt", "r", "utf-8-sig")
    lines = file.readlines()
    lines = [line.split(" - ") for line in lines]
    new_lines = []
    for subline in lines:
        for line in subline:
            new_lines.append(line.strip())
    team = new_lines[random.randint(0, len(new_lines))]
    return "\n\n" + chatgpt.ask("Скажи интересный фубольный факт о футбольной команде " + team) + "⚡⚡⚡"

# telegram_user_ids
# AAA - 475304200
# kolyalev - 212288934
# Tit - 5016952492
# Ryko - 683204699
# max - 451170390