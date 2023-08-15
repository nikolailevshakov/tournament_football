import requests
import telebot
import sql
import os

#TOKEN = open("token").read()
TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['пинг'])
def ping(message):
    bot.reply_to(message, "pong")


@bot.message_handler(commands=['хочумем'])
def get_meme(message):
    res = requests.get(" https://meme-api.com/gimme").json()
    meme = res['url']
    bot.reply_to(message, meme)


@bot.message_handler(commands=['помоги'])
def help(message):
    HELP_TEXT = "С первого раза не запомнил. Есть следующие команды: \n" \
           "/хочумем - получить рандомный мем с реддита\n" \
           "/регистрация - зарегистрироваться в турнире\n" \
           "/помоги - еще раз посмотреть все возможные команды"
    bot.send_message(message.chat.id, HELP_TEXT, parse_mode="Markdown")


@bot.message_handler(commands=['регистрация'])
def register(message):
    WELCOME_TEXT = "Привет! Введи через пробел свой юзернэйм и секретную фразу, которую будешь использовать при отправке прогноза в будующем! не используй " \
           "существующий пароль! Иначе создатель бота взломает все твои аккаунты"
    sent_username = bot.send_message(message.chat.id, WELCOME_TEXT, parse_mode="Markdown")
    bot.register_next_step_handler(sent_username, user_handler)


@bot.message_handler(commands=['прогноз'])
def prediction(message):
    TEXT = "Оставь свой прогноз на следующий тур в следующем формате: СЕКРЕТ, 12 49 27 64 19 23 21 87 62 42"
    send_prediction = bot.send_message(message.chat.id, TEXT)
    bot.register_next_step_handler(send_prediction, prediction_handler, parse_mode="Markdown")


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
        elif sql.number_users() > 4:
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
        sent_again = bot.send_message(
            message.chat.id, 'Ну все же, блять, написано. Пишем через ЗАПЯТУЮ!', parse_mode="Markdown")
        bot.register_next_step_handler(sent_again, prediction_handler)
    secret = res[0]
    prediction = res[1].split()
    if len(prediction) != 10:
        sent_again = bot.send_message(
            message.chat.id, 'Ну на 10 игр прогноз надо оставить, считать не умеешь? Давай заново.', parse_mode="Markdown")
        bot.register_next_step_handler(sent_again, prediction_handler)
    else:
        username, user_id = sql.get_userid(secret)
        sql.insert_prediction(prediction, user_id)

        text = "{username}, твой прогноз принят.".format(username=username)
        bot.send_message(message.chat.id, text, parse_mode="Markdown")