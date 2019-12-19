from src.db.db import get_conn_db
from pandas import DataFrame


def update_user(userId, won, time):
    db = get_conn_db()
    cursor = db.cursor()
    try:
        query = 'SELECT userId, played, won, lost, avgTime, bestTime, totalTime FROM user where userId = %s'
        value = (userId, )
        cursor.execute(query, value)
        df = DataFrame(cursor.fetchall())
        
        try:
            df.columns = ["userId", "played", "won", "lost", "avgTime", "bestTime", "totalTime"]

            played = df["played"][0]
            num_won = df["won"][0]
            num_lost = df["lost"][0]
            avgTime = df["avgTime"][0]
            bestTime = df["bestTime"][0]
            totalTime = df["totalTime"][0]
        except:
            played, num_won, num_lost, avgTime, bestTime, totalTime = (0, 0, 0, 0, 9999999, 0)

        played += 1

        if won:
            num_won += 1
            totalTime += time
            avgTime = totalTime/num_won
            if time < bestTime:
                bestTime = time
        else:
            num_lost += 1
        
        sql = "INSERT INTO user (userId, played, won, lost, avgTime, bestTime, totalTime) VALUES ('{}', {}, {}, {}, {}, {}, {}) ON DUPLICATE KEY UPDATE played={}, won={}, lost={}, avgTime = {}, bestTime = {}, totalTime = {}".format(userId, played, num_won, num_lost, avgTime, bestTime, totalTime, played, num_won, num_lost, avgTime, bestTime, totalTime)
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False

def update_list_users(users, winner, time):
    success = True 
    for user in users:
        success = True if update_user(user, user == winner, time) and success else False
    return success