import json
from src.db.db import mongodb as db
from src.db.db import mongoclient as conn 
import pandas as pd
from pymongo import MongoClient


def _connect_mongo(db):
    """ A util for making a connection to mongo """
    return conn[db]


def read_mongo(db, collection, query={}, no_id=True):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query)

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return df

def update_rank(users):
    df = read_mongo(db, 'rank')

