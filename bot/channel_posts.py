import envs
import requests
import utils
import sql
import results


# post_with_header("Четвертая неделя!", utils.read_games())
def post_with_header(header, message):
    chat_id = '-1001809163992'
    api_url = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'

    try:
        requests.post(api_url, json={'chat_id': chat_id, 'text': f'{header}\n{message}'})
    except Exception as e:
        print(e)


def check_if_prediction_exists():
    telegram_ids = sql.get_telegram_chat_ids()
    if utils.if_games_empty():
        return
    if sql.number_preds() == 5:
        return
    for telegram_id in telegram_ids:
        if not sql.check_user_pred_exists(telegram_id):
            notify_user(telegram_id)


def notify_user(telegram_user_id):
    api_url = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'
    try:
        requests.post(api_url, json={'chat_id': telegram_user_id, 'text': 'Прогноз собираешься оставлять?'})
    except Exception as e:
        print(e)


def notify_admin(message, username):
    admin_chat_id = '212288934'
    api_url = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'
    try:
        requests.post(api_url, json={'chat_id': admin_chat_id, 'text': f'Ошибка ❌ \n От {username}\n' + str(message)})
    except Exception as e:
        print(e)


def post_results():
    data = {}
    for item in sql.get_predictions():
        data.update({item[1]: {"prediction": item[0].split()}})
    for username, value in data.items():
        data[username]["current_points"] = results.calc_points(data[username]["prediction"],
                                                               data["results"]["prediction"])
    # get total points for users
    current_points = sql.get_points()
    for item in current_points:
        data[item[0]]['week_points'] = item[1]
        data[item[0]]['total_points'] = data[item[0]]['week_points'] + data[item[0]]["current_points"]
    post_text = "Участник || Неделя || Сезон \n"
    for username in data.keys():
        text_line = f'{username} || {data.username.week_points} || {data.username.total_points} \n'
        post_text += text_line
    post_with_header("Результаты недели!", post_text)
    return
