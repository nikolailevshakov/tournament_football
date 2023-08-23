import psycopg2
import queries


def connect_database(database: str):
    connection = psycopg2.connect(
        database=database, user='postgres', password='admin', host='localhost', port='5432'
    )
    connection.autocommit = True
    return connection


def disconnect_database(connection) -> None:
    connection.close()


def get_users() -> list:
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.GET_USERS)
    res = cursor.fetchall()
    usernames = [item[0] for item in res]
    disconnect_database(connection)
    return usernames


def insert_user(username: str, secret: str):
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.INSERT_USER.format(username=username, secret=secret))
    disconnect_database(connection)


def number_users() -> int:
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.NUMBER_USERS)
    num_users = cursor.fetchall()[0]
    disconnect_database(connection)
    return int(num_users[0])


def get_userid(secret) -> (str, str):
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.GET_USERNAME_USERID.format(secret=secret))
    res = cursor.fetchall()
    username, user_id = res[0][0], res[0][1]
    disconnect_database(connection)
    return username, user_id


def insert_prediction(prediction, user_id) -> None:
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.INSERT_PREDICTION.format(prediction=prediction, user_id=user_id))
    disconnect_database(connection)


def create_database() -> None:
    connection = connect_database("postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(queries.CREATE_DATABASE)
        print("INFO: Database tournament is created")
    except psycopg2.errors.DuplicateDatabase as e:
        print(e.pgerror)
    disconnect_database(connection)


def create_tables() -> None:
    connection = connect_database("tournament")
    cursor = connection.cursor()
    try:
        cursor.execute(queries.CREATE_USERS_TABLE)
        print("INFO: Table users is created")
    except psycopg2.errors.DuplicateTable as e:
        print(e.pgerror)

    try:
        cursor.execute(queries.CREATE_SEASON_TABLE)
        print("INFO: Table season is created")
    except psycopg2.errors.DuplicateTable as e:
        print(e.pgerror)

    try:
        cursor.execute(queries.CREATE_WEEK_TABLE)
        print("INFO: Table week is created")
    except psycopg2.errors.DuplicateTable as e:
        print(e.pgerror)

    disconnect_database(connection)


def delete_tables() -> None:
    connection = connect_database("tournament")
    cursor = connection.cursor()
    cursor.execute(queries.DROP_DATABASE)

    disconnect_database(connection)