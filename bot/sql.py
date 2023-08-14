import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='admin', host='127.0.0.1', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()


def get_users():
    conn = psycopg2.connect(
        database="tournament", user='postgres', password='admin', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    GET_USERS = "SELECT username from users;"
    cursor.execute(GET_USERS)
    res = cursor.fetchall()
    usernames = [item[0] for item in res]
    conn.close()
    return usernames


def insert_user(username, secret):
    conn = psycopg2.connect(
        database="tournament", user='postgres', password='admin', host='127.0.0.1', port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    INSERT_USER = "INSERT INTO users (username, secret) VALUES ('{username}', '{secret}');"\
        .format(username=username, secret=secret)
    cursor.execute(INSERT_USER)
    conn.close()


try:
    cursor.execute("CREATE DATABASE tournament")
    print("INFO: Database tournament is created")
except psycopg2.errors.DuplicateDatabase as e:
    print(e.pgerror)

conn.close()

conn = psycopg2.connect(
   database="tournament", user='postgres', password='admin', host='127.0.0.1', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()

CREATE_USERS_TABLE = "CREATE TABLE users (id SERIAL PRIMARY KEY, " \
                     "username VARCHAR(255), secret VARCHAR(255), created_at TIMESTAMP)"
CREATE_SEASON_TABLE = "CREATE TABLE season (id SERIAL PRIMARY KEY, " \
                      "week INT, user_id INT, CONSTRAINT FK_users_id FOREIGN KEY (user_id) REFERENCES users(id), " \
                      "points INT, created_at TIMESTAMP)"
CREATE_WEEK_TABLE = "CREATE TABLE current_week (id SERIAL PRIMARY KEY, " \
                    "prediction VARCHAR(255), user_id INT, " \
                    "CONSTRAINT FK_users_id FOREIGN KEY (user_id) REFERENCES users(id), " \
                    "results VARCHAR(255), created_at TIMESTAMP)"

try:
    cursor.execute(CREATE_USERS_TABLE)
    print("INFO: Table users is created")
except psycopg2.errors.DuplicateTable as e:
    print(e.pgerror)

try:
    cursor.execute(CREATE_SEASON_TABLE)
    print("INFO: Table season is created")
except psycopg2.errors.DuplicateTable as e:
    print(e.pgerror)

try:
    cursor.execute(CREATE_WEEK_TABLE)
    print("INFO: Table week is created")
except psycopg2.errors.DuplicateTable as e:
    print(e.pgerror)


conn.close()
