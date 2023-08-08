import mysql.connector

cnx = mysql.connector.connect(user='admin', password='password',
                              host='127.0.0.1')

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE tournament")

CREATE_USERS_TABLE = "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, " \
                     "username VARCHAR(255), secret VARCHAR(255), created_at TIMESTAMP)"
CREATE_SEASON_TABLE = "CREATE TABLE season (id INT AUTO_INCREMENT PRIMARY KEY, " \
                      "week INT, FOREIGN KEY (user_id) REFERENCES users(id), points INT, created_at TIMESTAMP)"
CREATE_WEEK_TABLE = "CREATE TABLE current_week (id INT AUTO INCREMENT PRIMARY KEY, " \
                    "prediction VARCHAR(255), FOREIGN KEY (user_id) REFERENCES users(id), " \
                    "results VARCHAR(255), created_at TIMESTAMP)"

cursor.execute(CREATE_USERS_TABLE)
cursor.execute(CREATE_SEASON_TABLE)
cursor.execute(CREATE_WEEK_TABLE)


cnx.close()
