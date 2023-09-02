import sql
import codecs
import calcPoints


def output_predictions():
    res = sql.get_predictions()
    with codecs.open("files/predictions.txt", "w", "utf-8-sig") as f:
        for item in res:
            f.write("{username}, {prediction} \n".
                    format(username=item[0],
                           prediction=item[1]))


output_predictions()
calcPoints.output_results()
