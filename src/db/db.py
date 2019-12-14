import mysql.connector
from os import environ

user_db = environ.get("MYSQL_USER")
pass_db = environ.get("MYSQL_PASSWORD")
url_db = environ.get("DB_URL")

db = mysql.connector.connect(
  host=url_db,
  user=user_db,
  passwd=pass_db
)