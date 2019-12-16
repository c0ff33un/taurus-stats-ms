from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

user_db = environ.get("MYSQL_USER")
pass_db = environ.get("MYSQL_PASSWORD")
url_db = environ.get("DB_URL")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + user_db + ":" + pass_db + "@" + url_db + "/taurus-stats"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=False)
    played = db.Column(db.Integer)
    won = db.Column(db.Integer)
    lost = db.Column(db.Integer)
    totalTime = db.Column(db.Integer) # Total time spend resolving all mazes
    avgTime = db.Column(db.Integer)
    bestTime = db.Column(db.Integer)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totalGames = db.Column(db.Integer)
    totalPlayers = db.Column(db.Integer)

if __name__ == '__main__':
    manager.run()