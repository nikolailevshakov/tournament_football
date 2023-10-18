

# def calc_points(game_preds: list[str], results: list[str]) -> int:
def calc_points(game_preds, results) -> int:
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
