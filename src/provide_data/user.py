from src.db.db import db
from pandas import DataFrame

cursor = db.cursor()

def get_user(userId):
    cursor.execute('SELECT * FROM user where userId = %s', (userId,))
    df = DataFrame(cursor.fetchall())
    try:
        df.columns = ["userId", "played", "won", "lost", "avgTime", "bestTime", "totalTime"]

        played = df["played"][0]
        num_won = df["won"][0]
        num_lost = df["lost"][0]
        avgTime = df["avgTime"][0]
        bestTime = df["bestTime"][0]
    except:
        played, num_won, num_lost, avgTime, bestTime = (0, 0, 0, 0, 9999999)

    if bestTime == 9999999:
        bestTime = 0

    
    return int(played), int(num_won), int(num_lost), int(avgTime), int(bestTime)
