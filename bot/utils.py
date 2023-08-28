import codecs


def read_games():
    file = codecs.open("./files/games.txt", "r", "utf-8-sig")
    lines = file.readlines()
    return "\n".join(lines)
