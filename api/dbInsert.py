# Get the database using the method we defined in pymongo_test_insert file
from dbGet import get_database


def db_insert(userEmail):
    print("Inside db_insert...")
    wenevrdb = get_database()
    users = wenevrdb["users"]
    print(users)

    new_user = {
        "email": userEmail,
        "level": 1,
        "dictionary": {"foo": "bar", "boo": "nar"},
        "stats": {"progress": {}, "correct": 0, "incorrect": 0}
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
    currentStats = activeUser['stats']
    currentProgress = currentStats['progress']
    currentCorrect = currentStats['correct']
    currentIncorrect = currentStats['incorrect']
    newProgress = 0
    if word in currentProgress:
        wordProgress = currentProgress[word]
        wordProgress += 1
        newProgress = wordProgress
    else:
        newProgress += 1
    currentProgress.update({word: newProgress})
    currentCorrect += 1
    newStats = {"progress": currentProgress,
                "correct": currentCorrect, "incorrect": currentIncorrect}
    valueToUpdate = {"$set": {"stats": newStats}}

    users.update_one(queryByEmail, valueToUpdate)


def add_to_incorrect(userEmail):
    wenevrdb = get_database()
    users = wenevrdb["users"]
    queryByEmail = {"email": userEmail}
    userQuery = wenevrdb.users.find(queryByEmail)
    activeUser = {}
    for user in userQuery:
        print(user)
        activeUser = user

    currentStats = activeUser['stats']
    currentProgress = currentStats['progress']
    currentCorrect = currentStats['correct']
    print("USER")
    print(currentStats)
    currentIncorrect = currentStats['incorrect']  # returns int count.
    print("current incorrect")
    print(currentIncorrect)
    currentIncorrect += 1
    currentStats['incorrect'] = currentIncorrect
    print("new incorrect")
    print(currentIncorrect)
    newStats = {"progress": currentProgress,
                "correct": currentCorrect, "incorrect": currentIncorrect}
    valueToUpdate = {"$set": {"stats": newStats}}

    users.update_one(queryByEmail, valueToUpdate)
    return
