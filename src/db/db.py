import mysql.connector
import pymongo
import os

db = mysql.connector.connect(
  host=os.environ['DB_URL'],
  user=os.environ['MYSQL_USER'],
  passwd=os.environ['MYSQL_PASSWORD'],
  database=os.environ['MYSQL_DATABASE'],
)

mongoclient = pymongo.MongoClient('mongodb://' + os.environ['MONGO_URL'] + '/')

mongodb = mongoclient['ranking']