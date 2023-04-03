# Get the database using the method we defined in pymongo_test_insert file
from dateutil import parser
from dbGet import get_database


def db_insert(userEmail):
    print("Inside db_insert...")
    wenevrdb = get_database()
    users = wenevrdb["users"]
    print(users)

    new_user = {
        "email": userEmail,
        "level": 0,
        "dictionary": {"foo": "bar", "boo": "nar"},
        "progress": {}
    }
    users.insert_one(new_user)


def update_progress(userEmail, word):
    print("Inside userProgress")
    wenevrdb = get_database()
    users = wenevrdb["users"]
    queryByEmail = {"email": userEmail}
    userQuery = wenevrdb.users.find(queryByEmail)
    activeUser = {}
    for user in userQuery:
        print(user)
        activeUser = user

    # currentProgress = {"汉字": int, ...}
    currentProgress = activeUser['progress']
    newProgress = 0
    if word in currentProgress:
        wordProgress = currentProgress[word]
        wordProgress += 1
        newProgress = wordProgress
    else:
        newProgress += 1
    currentProgress.update({word: newProgress})
    valueToUpdate = {"$set": {"progress": currentProgress}}

    users.update_one(queryByEmail, valueToUpdate)
