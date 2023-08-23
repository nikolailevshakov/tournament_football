import requests
import telebot
import sql, texts
import os

TOKEN = open("token").read()
#TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['пинг'])
def ping(message):
    try:
        bot.reply_to(message, "pong")
    except Exception as e:
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['хочумем'])
def get_meme(message):
    try:
        res = requests.get(" https://meme-api.com/gimme").json()
        meme = res['url']
        bot.reply_to(message, meme)
    except Exception as e:
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['помоги'])
def help(message):
    try:
        bot.send_message(message.chat.id, texts.HELP, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, "Ошибочка, сорян")

@bot.message_handler(commands=['регистрация'])
def register(message):
    try:
        sent_username = bot.send_message(message.chat.id, texts.WELCOME, parse_mode="Markdown")
        bot.register_next_step_handler(sent_username, user_handler)
    except Exception as e:
        bot.reply_to(message, "Ошибочка, сорян")


@bot.message_handler(commands=['прогноз'])
def prediction(message):
    try:
        send_prediction = bot.send_message(message.chat.id, texts.PREDICTION)
        bot.register_next_step_handler(send_prediction, prediction_handler)
    except Exception as e:
        bot.reply_to(message, "Ошибочка, сорян")


def user_handler(message: str):
    res = message.text.split()
    if len(res) != 2:
        sent_again = bot.send_message(
            message.chat.id, 'Сразу видно, что в Нижне Омринской средней учился. Пиши юзернейм ПРОБЕЛ секрет', parse_mode="Markdown")
        bot.register_next_step_handler(sent_again, user_handler)
    else:
        username = res[0]
        secret = res[1]
        if sql.get_users() is not None and username in sql.get_users():
            sent_again = bot.send_message(
                message.chat.id, 'Такой юзернейм уже занят! Хреновая у вас фантазия. Выбирай другой!',
                parse_mode="Markdown")
            bot.register_next_step_handler(sent_again, user_handler)
        elif sql.number_users() > 5:
            ERROR_TEXT = 'Все свои уже зарегались. Ты кто такой, парниша?'
            bot.send_message(message.chat.id, ERROR_TEXT, parse_mode="Markdown")
        else:
            sql.insert_user(username, secret)
            text = "Поздравляю, {username} Ты зарегистрирован. Твоя секретная фраза: {secret}".format(username=username, secret=secret)
            bot.send_message(
                message.chat.id, text, parse_mode="Markdown")


def prediction_handler(message: str):
    res = message.text.split(',')
    if len(res) != 2:
        bot.send_message(
            message.chat.id, 'Ну все же, блять, написано. Пишем через ЗАПЯТУЮ! Заново - /прогноз', parse_mode="Markdown")
        return
    secret = res[0]
    prediction = res[1].split()
    if len(prediction) != 10:
        bot.send_message(
            message.chat.id, 'Ну на 10 игр прогноз надо оставить, считать не умеешь? Давай заново - /прогноз',  parse_mode="Markdown")
        return
    else:
        try:
            username, user_id = sql.get_userid(secret)
        except IndexError as e:
            bot.send_message(
                message.chat.id, 'Секрет свой забыл? Ну ты блять и гений. Админу пиши. Или начинай сначала - /прогноз.',
                parse_mode="Markdown")
            return
        sql.insert_prediction(" ".join(prediction), user_id)

        text = "{username}, твой прогноз принят.".format(username=username)
        bot.send_message(message.chat.id, text)