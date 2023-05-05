from pymongo import MongoClient
import os
from decouple import config
# tryeryr
# TRY 2


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = config('MONGODB_SECRET')

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    print(client['wenevrdb'])

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['wenevrdb']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    wenevrdb = get_database()
