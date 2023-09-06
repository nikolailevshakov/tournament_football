import envs
import requests
import utils
import sql
import results


#post_with_header("Четвертая неделя!", utils.read_games())
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
        requests.post(api_url, json={'chat_id': admin_chat_id, 'text':f'Ошибка ❌ \n От {username}\n'+str(message)})
    except Exception as e:
        print(e)


def post_results():
    # get dict of username and prediction list
    # get list of results
    # for username in dict:
    #     dict[username][result] = results.calc_points(preds, results_list)
    # get total points for users
    # insert updated points to sql table
    # generate post
    # post_with_header("Результаты!", sql.get_results)
    pass
