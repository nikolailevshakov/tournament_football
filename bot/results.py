import codecs
import sql


def calc_points(game_preds: list[str], results: list[str]) -> int:
    points = 0
    for i in range(len(game_preds)):
        if results[i] == '':
            continue
        if game_preds[i] == results[i]:
            points += 3
        elif int(game_preds[i][0])-int(game_preds[i][1]) \
                == int(results[i][0])-int(results[i][1]):
            points += 2
        elif (int(game_preds[i][0])-int(game_preds[i][1])) > 0\
                and (int(results[i][0])-int(results[i][1])) > 0:
            points += 1
        elif (int(game_preds[i][0]) - int(game_preds[i][1])) < 0\
                and (int(results[i][0]) - int(results[i][1])) < 0:
            points += 1
        else:
            continue
    return points


def output_predictions() -> dict:
    query = sql.get_predictions()
    result = {}
    with codecs.open("files/predictions.txt", "w", "utf-8-sig") as f:
        for item in query:
            result[item[0]] = item[1]
    return result


def output_results() -> list[str]:
    return sql.get_results().split()

print(calc_points(["11", "21", "20", "20", "11", "21", "12", "31", "13"], ["20", "12", "21", "01", "31", "40", "11", "32" ,"14"]), "tit")
print(calc_points(["22", "31", "20", "20", "31", "30", "12", "31", "21"], ["20", "12", "21", "01", "31", "40", "11", "32" ,"14"]), "ryk")
print(calc_points(["11", "20", "10", "20", "21", "31", "10", "21", "11"], ["20", "12", "21", "01", "31", "40", "11", "32" ,"14"]), "ali")
print(calc_points(["22", "21", "20", "31", "21", "21", "12", "20", "22"], ["20", "12", "21", "01", "31", "40", "11", "32" ,"14"]), "max")
print(calc_points(["23", "20", "31", "10", "21", "20", "11", "10", "02"], ["20", "12", "21", "01", "31", "40", "11", "32" ,"14"]), "lev")
