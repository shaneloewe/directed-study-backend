from dbGet import get_database
import config
import random as rand


def get_userid(userEmail):
    # Get the database using the method we defined in pymongo_test_insert file
    wenevrdb = get_database()
    # print("Inside the get_userId Function")
    # print("User email:"+userEmail)

    collections = wenevrdb.list_collection_names()
    # print("collections: ", collections, "\n")

    users = wenevrdb["users"]
    userQuery = wenevrdb.users.find({"email": userEmail})
    foundUser = 0
    for item in userQuery:
        # print("Email we found: "+str(item["email"]))
        foundUser += 1
    if foundUser == 1:
        return True
    else:
        return False
    # Note that this is the Global currentUser var

    # for atr in config.currentUser:
    # print(str(atr['_id']))
    # return str(atr['_id'])
    # Returns str value of _id


def get_userdict(userEmail):
    wenevrdb = get_database()
    collections = wenevrdb.list_collection_names()
    users = wenevrdb["users"]
    userQuery = wenevrdb.users.find({"email": userEmail})
    for u in userQuery:
        return u['dictionary']


def get_profile_stats(userEmail):
    wenevrdb = get_database()
    collections = wenevrdb.list_collection_names()
    users = wenevrdb["users"]
    userQuery = wenevrdb.users.find({"email": userEmail})
    for u in userQuery:
        return u['progress']


def get_userLevel(userEmail):
    wenevrdb = get_database()
    collections = wenevrdb.list_collection_names()
    users = wenevrdb["users"]
    userQuery = wenevrdb.users.find({"email": userEmail})
    for u in userQuery:
        print(u['level'])
        # Should be integer ^^ i think
        return u['level']


def get_word(userLevel):
    wenevrdb = get_database()
    collections = wenevrdb.list_collection_names()
    words = wenevrdb["words"]
    wordQuery = wenevrdb.words.find({"level": userLevel})
    collSize = wenevrdb.words.count_documents({})
    # print(collSize)
    selector = rand.randint(0, collSize-1)
    # print("Selector: "+str(selector))
    counter = 0
    for word in wordQuery:
        # print(word['hanzi'])
        if counter == selector:
            return word['hanzi']
        else:
            counter += 1


def get_sentence(word, userLevel):
    print()
    print("Inside GetSentence")
    print("Here's the word we've selected: "+word)
    print("Here's the userLevel: "+str(userLevel))
    print()
    wenevrdb = get_database()
    collections = wenevrdb.list_collection_names()
    sentences = wenevrdb["sentences"]
    sentenceQuery = wenevrdb.sentences.find(
        {"$and": [
            {"level": userLevel},
            {"hanzi": {"$regex": word}}
        ]}
    )
    sentencesContainingWord = []
    for sentence in sentenceQuery:
        print(sentence)
        sentencesContainingWord.append(sentence)

    packagedSentences = []
    # Pick 3 sentences
    if len(sentencesContainingWord) >= 3:
        packagedSentences = rand.sample(sentencesContainingWord, 3)
    else:
        print()
        print("We don't have enough sentences to make that request")
        print()
    print("Here are the 3 words we selected: ")
    for sentence in packagedSentences:
        sentence['_id'] = str(sentence['_id'])
        print(sentence)
    print()
    return packagedSentences


def return_all():
    # Get the database using the method we defined in pymongo_test_insert file
    wenevrdb = get_database()

    collections = wenevrdb.list_collection_names()
    print("collections: ", collections, "\n")

    users = wenevrdb["users"]
    userQuery = wenevrdb.users.find()
    for item in userQuery:
        print(item)
    return ""
    # Note that this is the Global currentUser var

    # for atr in config.currentUser:
    # print(str(atr['_id']))
    # return str(atr['_id'])
    # Returns str value of _id
