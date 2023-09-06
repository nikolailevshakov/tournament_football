GET_USERS = "SELECT username from users;"
CREATE_DATABASE = "CREATE DATABASE tournament"
CREATE_USERS_TABLE = "CREATE TABLE users (id SERIAL PRIMARY KEY, " \
                         "username VARCHAR(255), " \
                     "secret VARCHAR(255), " \
                     "telegram_user_id VARCHAR(255)," \
                     "created_at TIMESTAMP)"
CREATE_SEASON_TABLE = "CREATE TABLE season (id SERIAL PRIMARY KEY, " \
                          "week INT, user_id INT, " \
                      "CONSTRAINT FK_users_id FOREIGN KEY " \
                      "(user_id) REFERENCES users(id), " \
                          "points INT, created_at TIMESTAMP)"
CREATE_WEEK_TABLE = "CREATE TABLE current_week (id SERIAL PRIMARY KEY, " \
                        "prediction VARCHAR(255), user_id INT, " \
                        "CONSTRAINT FK_users_id FOREIGN KEY" \
                    " (user_id) REFERENCES users(id), " \
                        "results VARCHAR(255), created_at TIMESTAMP)"
DROP_DATABASE = "DROP DATABASE IF EXISTS tournament"
INSERT_USER = "INSERT INTO users (username, telegram_user_id) VALUES ('{username}', '{telegram_user_id}');"
NUMBER_USERS = "SELECT COUNT(*) FROM users"
INSERT_PREDICTION = "INSERT INTO current_week (prediction, user_id) VALUES ('{prediction}', '{user_id}')"
GET_USERNAME_USERID = "SELECT username, id FROM users WHERE telegram_user_id='{telegram_user_id}'"
GET_PREDICTION_USERNAME = "SELECT users.username, prediction FROM current_week " \
                          "INNER JOIN users ON users.id = current_week.user_id"
CLEAR_WEEK_TABLE = "DELETE FROM current_week"

ADD_POINTS = "INSERT INTO season (week, user_id, points) VALUES (1, '{user_id}', '{points}');"

GET_PREDICTIONS = "SELECT current_week.prediction, users.username FROM current_week " \
                  "INNER JOIN users on users.id = current_week.user_id"

GET_RESULTS = "SELECT current_week.prediction FROM current_week " \
              "WHERE current_week.user_id=999"

NUMBER_PREDS = "SELECT COUNT(*) FROM current_week"

USER_PRED = "SELECT current_week.prediction FROM current_week " \
            "WHERE current_week.user_id={user_id}"

TELEGRAM_IDS = "SELECT telegram_user_id FROM users " \
               "WHERE id != 7"
