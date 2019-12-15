from src.db.db import db
from pandas import DataFrame

cursor = db.cursor()

def update_user(userId, won):
    try:
        query = 'SELECT * FROM user where userId = %s'
        value = (userId, )
        cursor.execute(query, value)
        df = DataFrame(cursor.fetchall())
        try:
            df.columns = ["userId", "played", "won", "lost"]

            played, num_won, num_lost = (df["played"][0] if df["played"][0] is not None else 0, df["won"][0] if df["won"][0] is not None else 0, df["lost"][0] if df["lost"][0] is not None else 0)
        except:
            played, num_won, num_lost = (0, 0, 0)
        if won:
            num_won += 1
        else:
            num_lost += 1
        
        sql = "INSERT INTO user (userId, played, won, lost) VALUES ({}, {}, {}, {}) ON DUPLICATE KEY UPDATE played={}, won={}, lost={}".format(userId, played + 1, num_won, num_lost, played + 1, num_won, num_lost)
        cursor.execute(sql)
        db.commit()
        return True
    except:
        return False  

def update_list_users(users, winner):
    success = True 
    for user in users:
        success = True if update_user(user, user == winner) and success else False
    return success