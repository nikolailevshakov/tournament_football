import codecs


def calc_points(game_preds: list[str], results: list[str]) -> int:
    points = 0
    for i in range(len(game_preds)):
        if results[i] == '': continue
        if game_preds[i] == results[i]:
            points += 3
        elif int(game_preds[i][0])-int(game_preds[i][1]) == int(results[i][0])-int(results[i][1]):
            points += 2
        elif (int(game_preds[i][0])-int(game_preds[i][1])) > 0 and (int(results[i][0])-int(results[i][1])) > 0:
            points += 1
        elif (int(game_preds[i][0]) - int(game_preds[i][1])) < 0 and (int(results[i][0]) - int(results[i][1])) < 0:
            points += 1
        else:
            continue
    return points


def read_result():
    file = open("files/results.txt", "r")
    return file.readline().strip('\n')


def output_results():
    results = [game_result for game_result in read_result().split()]
    file = codecs.open("files/predictions.txt", "r", "utf-8-sig")
    lines = file.readlines()
    for line in lines:
        prediction, username = line.split(",")[0], line.split(",")[1]
        points = calc_points([game_prediction for game_prediction in prediction.split()], results)
        print("User {username}, points {points}\n".format(username=username, points=points))
