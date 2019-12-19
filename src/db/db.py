import mysql.connector
import os

def get_conn_db():
  return mysql.connector.connect(
    host=os.environ['DB_URL'],
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
  )