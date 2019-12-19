from src.db.db import get_conn_db
from pandas import DataFrame
import json


def global_ranker():
    db = get_conn_db()
    cursor = db.cursor()
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
    db = get_conn_db()
    cursor = db.cursor()
    # try:
    query = 'SELECT * FROM ( SELECT userId, avgTime, @curRank := @curRank + 1 AS rank FROM user, (SELECT @curRank := 0) r where avgTime != 0 ORDER BY  avgTime) rank where rank.userId = \'{}\' limit 100;'.format(userId)
    cursor.execute(query)
    df = DataFrame(cursor.fetchall())
    df.columns = ["userId", "avgTime", "rank"]
    j = df.to_json(orient='index')
    return json.loads(j)
    # except:
    #     return False