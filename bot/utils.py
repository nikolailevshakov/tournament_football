import codecs
import os


def read_games():
    file = codecs.open("./files/games.txt", "r", "utf-8-sig")
    lines = file.readlines()
    return "".join(lines)


def clear_games():
    open('./files/games.txt', 'w').close()


def if_games_empty():
    return os.path.getsize("./files/games.txt") == 0
