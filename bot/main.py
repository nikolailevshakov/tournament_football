import telebot, requests

TOKEN = open("token").read()


bot = telebot.TeleBot(TOKEN)

data = {}


@bot.message_handler(commands=['пинг'])
def send_welcome(message):
    bot.reply_to(message, "pong")


@bot.message_handler(commands=['хочумем'])
def send_welcome(message):
    res = requests.get(" https://meme-api.com/gimme").json()
    meme = res['url']
    bot.reply_to(message, meme)


@bot.message_handler(commands=['помоги'])
def register(message):
    HELP_TEXT = "С первого раза не запомнил. Есть следующие команды: \n" \
           "/хочумем - получить рандомный мем с реддита\n" \
           "/регистрация - зарегистрироваться в турнире\n" \
           "/помоги - еще раз посмотреть все возможные команды"
    sent_username = bot.send_message(message.chat.id, HELP_TEXT, parse_mode="Markdown")


@bot.message_handler(commands=['регистрация'])
def register(message):
    WELCOME_TEXT = "Привет! Введи через пробел свой юзернэйм и секретную фразу, которую будешь использовать при отправке прогноза в будующем! не используй " \
           "существующий пароль! Иначе создатель бота взломает все твои аккаунты"
    sent_username = bot.send_message(message.chat.id, WELCOME_TEXT, parse_mode="Markdown")
    bot.register_next_step_handler(sent_username, user_handler)


def user_handler(message):
    res = message.text.split()
    if len(res) != 2:
        sent_again = bot.send_message(
            message.chat.id, 'Сразу видно, что в Нижне Омринской средней учился. Пиши юзернейм ПРОБЕЛ секрет', parse_mode="Markdown")
        bot.register_next_step_handler(sent_again, user_handler)
    else:
        username = res[0]
        secret = res[1]
        print(username, secret)
        if username in data:
            sent_again = bot.send_message(
                message.chat.id, 'Такой юзернейм уже занят! Вот это у вас фантазия. Выбирай другой!',
                parse_mode="Markdown")
            bot.register_next_step_handler(sent_again, user_handler)
        else:
            data[username] = secret
            text = "Поздравляю, {username} Ты зарегистрирован. Твоя секретная фраза: {secret}".format(username=username, secret=secret)
            bot.send_message(
                message.chat.id, text, parse_mode="Markdown")
        print(data)


bot.infinity_polling()