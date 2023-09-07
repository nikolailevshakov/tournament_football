import psycopg2
import queries
import envs


db = envs.DATABASE


def connect_database(database: str):
    connection = psycopg2.connect(
        database=database,
        user=envs.POSTGRES_USER,
        password=envs.POSTGRES_PASSWORD,
        host=envs.DATABASE_HOST,
        port=envs.DATABASE_PORT
    )
    connection.autocommit = True
    return connection


def disconnect_database(connection) -> None:
    connection.close()


def get_users(database=db) -> list:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.GET_USERS)
    res = cursor.fetchall()
    usernames = [item[0] for item in res]
    disconnect_database(connection)
    return usernames


def insert_user(username: str, secret: str, database=db):
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.INSERT_USER.format(username=username, secret=secret))
    disconnect_database(connection)


def number_users(database=db) -> int:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.NUMBER_USERS)
    num_users = cursor.fetchall()[0]
    disconnect_database(connection)
    return int(num_users[0])


def get_userid(telegram_user_id, database=db) -> (str, str):
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.GET_USERNAME_USERID.format(telegram_user_id=telegram_user_id))
    res = cursor.fetchall()
    username, user_id = res[0][0], res[0][1]
    disconnect_database(connection)
    return username, user_id


def insert_prediction(prediction, user_id, database=db) -> None:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.INSERT_PREDICTION.format(prediction=prediction, user_id=user_id))
    disconnect_database(connection)


def get_predictions(database=db):
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.GET_PREDICTIONS)
    res = cursor.fetchall()
    disconnect_database(connection)
    return res


def get_results(database=db):
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.GET_RESULTS)
    res = cursor.fetchall()
    disconnect_database(connection)
    return res[0][0]


def create_database(database=db) -> None:
    connection = connect_database(database)
    cursor = connection.cursor()
    try:
        cursor.execute(queries.CREATE_DATABASE)
        print("INFO: Database tournament is created")
    except psycopg2.errors.DuplicateDatabase as e:
        print(e.pgerror)
    disconnect_database(connection)


def create_tables(database=db) -> None:
    connection = connect_database(database)
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


def delete_tables(database=db) -> None:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.DROP_DATABASE)
    disconnect_database(connection)


def clear_current_week(database=db) -> None:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.CLEAR_WEEK_TABLE)
    disconnect_database(connection)


def number_preds(database=db) -> int:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.NUMBER_PREDS)
    num_preds = cursor.fetchall()[0]
    disconnect_database(connection)
    return int(num_preds[0])


def check_user_pred_exists(telegram_user_id: str, database=db) -> bool:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.USER_PRED.format(user_id=telegram_user_id))
    user_pred = cursor.fetchall()
    disconnect_database(connection)
    return bool(user_pred)


def get_telegram_chat_ids(database=db) -> [str]:
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.TELEGRAM_IDS)
    telegram_ids = cursor.fetchall()
    disconnect_database(connection)
    return [telegram_user_id[0] for telegram_user_id in telegram_ids]


def get_points(database=db):
    connection = connect_database(database)
    cursor = connection.cursor()
    cursor.execute(queries.GET_POINTS)
    points = cursor.fetchall()
    disconnect_database(connection)
    return points