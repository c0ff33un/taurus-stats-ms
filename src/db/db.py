import mysql.connector
import os

db = mysql.connector.connect(
  host=os.environ['DB_URL'],
  user=os.environ['MYSQL_USER'],
  passwd=os.environ['MYSQL_PASSWORD'],
  database=os.environ['MYSQL_DATABASE'],
)