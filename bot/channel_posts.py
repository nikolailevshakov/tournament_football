import envs
import requests
import utils
import sql
import results
import sys
import chatgpt
sys.stdout.reconfigure(encoding='utf-8')


# post_with_header("Четвертая неделя!", utils.read_games())
def post_with_header(header, message):
    chat_id = '-1001809163992'
    api_url = f'https://api.telegram.org/bot{envs.TOKEN}/sendMessage'

    try:
        requests.post(api_url, json={'chat_id': chat_id, 'text': f'{header}\n\n{message}'})
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
    week_points = {}
    total_points = {}
    data = {}
    for item in sql.get_predictions():
        data.update({item[1]: {"prediction": item[0].split()}})
    for username in data.keys():
        week_points[username]= results.calc_points(data[username]["prediction"],
                                                               data["results"]["prediction"])
    previous_points = sql.get_points()

    for item in previous_points:
        total_points[item[0]] = week_points[item[0]] + item[1]
    all_texts = []
    for username in data.keys():
        if username != "results":
            text_line = [username, week_points[username], total_points[username]]
            all_texts.append(text_line)
            sql.update_points(username, total_points[username])
    table = utils.organize_results(all_texts)
    post_text = table + "\n\nФутбольный факт: " + chatgpt.ask("Скажи интересный фубольный факт") + "🙅‍♂️⚽"
    print(post_text)
    post_with_header("🌟📊Результаты недели!📊🌟", post_text)
    return
