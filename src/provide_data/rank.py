from src.db.db import db
from pandas import DataFrame
import json

cursor = db.cursor()

def global_ranker():
    try:
        query = 'SELECT * FROM ( SELECT userId, avgTime, @curRank := @curRank + 1 AS rank FROM user, (SELECT @curRank := 0) r where avgTime != 0 ORDER BY  avgTime) rank limit 100'
        cursor.execute(query)
        df = DataFrame(cursor.fetchall())
        df.columns = ["userId", "avgTime", "rank"]
        j = df.to_json(orient='index')
        return json.loads(j)
    except:
        return False

def user_rank(userId):
    try:
        query = 'SELECT * FROM ( SELECT userId, avgTime, @curRank := @curRank + 1 AS rank FROM user, (SELECT @curRank := 0) r where avgTime != 0 ORDER BY  avgTime) rank where rank.userId = {} limit 100;'.format(userId)
        cursor.execute(query)
        df = DataFrame(cursor.fetchall())
        df.columns = ["userId", "avgTime", "rank"]
        j = df.to_json(orient='index')
        return json.loads(j)
    except:
        return False