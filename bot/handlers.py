import requests
import telebot
import sql
import texts
import utils
import envs
import channel_posts
import chatgpt
import logging

bot = telebot.TeleBot(envs.TOKEN)

MENU = ["хочумем", "помоги", "прогноз", "поговорить"]


@bot.message_handler(commands=['пинг'])
def ping(message):
    print('from_user_id: {id}, username: {username}, chatid: {chat_id}, first_name: {first_name}'.
          format(id=message.from_user.id, username=message.from_user.username, chat_id=message.chat.id, first_name=message.from_user.first_name))
    try:
        bot.reply_to(message, "понг")
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['хочумем'])
def get_meme(message):
    try:
        res = requests.get(" https://meme-api.com/gimme").json()
        meme = res['url']
        bot.reply_to(message, meme)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['помоги'])
def help(message):
    try:
        bot.send_message(message.chat.id, texts.HELP,
                         parse_mode="Markdown")
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['регистрация'])
def register(message):
    try:
        sent_username = bot.send_message(message.chat.id,
                                         texts.WELCOME,
                                         parse_mode="Markdown")
        bot.register_next_step_handler(sent_username,
                                       user_handler)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['прогноз'])
def prediction(message):
    if utils.if_games_empty():
        bot.reply_to(message, "Игр нет, какой прогноз собрался оставить, фраерок?")
        return
    try:
        games = utils.read_games()
        bot.send_message(message.chat.id, texts.PREDICTION)
        send_prediction = bot.send_message(message.chat.id, games)
        bot.register_next_step_handler(send_prediction, prediction_handler)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['результаты'])
def results(message):
    if message.chat.id != 212288934:
        bot.reply_to(message, "Ну и куда полез. Тебе нельзя пользоваться этой командой.")
        return
    games = utils.read_games()
    try:
        send_results = bot.send_message(message.chat.id, texts.RESULTS + games)
        bot.register_next_step_handler(send_results, results_handler)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['поговорить'])
def talk(message):
    try:
        bot.send_message(message.chat.id, utils.talk_response(),
                         parse_mode="Markdown")
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['игры'])
def talk(message):
    if message.chat.id != 212288934:
        bot.reply_to(message, "Ну и куда полез. Тебе нельзя пользоваться этой командой.")
        return
    try:
        send_games = bot.send_message(message.chat.id, texts.GAMES)
        bot.register_next_step_handler(send_games, games_handler)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler()
def default(message):
    try:
        bot.send_message(message.chat.id, chatgpt.ask(message.text) + "\n\n" + texts.WHAT_DO, parse_mode="Markdown")
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message,
                     "Ошибочка, сорян")


def results_handler(message):
    results = message.text.split()
    if len(results) != 10:
        bot.send_message(
            message.chat.id, 'Ну на 10 игр прогноз надо оставить, считать не умеешь? '
                             'Давай заново - /результаты', parse_mode="Markdown")
        return
    sql.insert_prediction(message.text, "6")
    bot.send_message(message.chat.id, "Готово!")


def games_handler(message):
    try:
        utils.write_games(message.text)
    except Exception as e:
        channel_posts.notify_admin(e, message.from_user.username)
        bot.reply_to(message,
                     "Ошибочка, сорян")
    finally:
        bot.send_message(message.chat.id, "Готово!")


def user_handler(message):
    res = message.text.split()
    if len(res) != 2:
        sent_again = bot.send_message(
            message.chat.id,
            'Сразу видно, что в Нижне Омринской средней учился. Пиши юзернейм ПРОБЕЛ секрет',
            parse_mode="Markdown")
        bot.register_next_step_handler(sent_again, user_handler)
    else:
        username = res[0]
        if sql.get_users() is not None and username in sql.get_users():
            sent_again = bot.send_message(
                message.chat.id, 'Такой юзернейм уже занят! Хреновая у вас фантазия. Выбирай другой!',
                parse_mode="Markdown")
            bot.register_next_step_handler(sent_again, user_handler)
        elif sql.number_users() > 5:
            ERROR_TEXT = 'Все свои уже зарегались. Ты кто такой, парниша?'
            bot.send_message(message.chat.id,
                             ERROR_TEXT,
                             parse_mode="Markdown")
        else:
            sql.insert_user(username, message.chat.id)
            text = "Поздравляю, {username} Ты зарегистрирован. ".format(username=username)
            bot.send_message(
                message.chat.id, text, parse_mode="Markdown")


def prediction_handler(message):

    prediction = message.text.split()
    print(prediction)
    if len(prediction) != 10:
        bot.send_message(
            message.chat.id, 'Ну на 10 игр прогноз надо оставить, считать не умеешь?'
                             ' И про секретную фразу забудь! Пиши только прогноз. '
                             'Давай заново - /прогноз',  parse_mode="Markdown")
        return
    else:
        try:
            username, user_id = sql.get_userid(message.chat.id)
        except IndexError as e:
            channel_posts.notify_admin(e, message.from_user.username)

        sql.insert_prediction(" ".join(prediction), user_id)
    mess = 'pred: {pred}, username: {username}, chatid: {chat_id}, first_name: {first_name}'.format(pred=prediction, username=message.from_user.username, chat_id=message.chat.id,first_name=message.from_user.first_name)
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug(mess)
    text = "{username}, твой прогноз принят.".format(username=username)
    bot.send_message(message.chat.id, text)
