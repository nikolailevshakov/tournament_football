from handlers import bot
import sql


if __name__ == '__main__':
    sql.create_database()
    sql.create_tables()
    sql.get_userid('pass')
    bot.infinity_polling()