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


def multipleChoicePick(sentencesContainingWord, numOfSentencesToPick):
    packagedSentences = []
    # Pick # sentences
    if len(sentencesContainingWord) >= numOfSentencesToPick:
        packagedSentences = rand.sample(
            sentencesContainingWord, numOfSentencesToPick)
    else:
        print()
        print("We don't have enough sentences to make that request")
        print()
    print("Here are the words we selected: ")
    for sentence in packagedSentences:
        sentence['_id'] = str(sentence['_id'])
        print(sentence)
    print()
    return packagedSentences


def splitSentence(packagedSentences):
    arrOfNodeData = []
    for sentence in packagedSentences:
        print(len(sentence.get("hanzi")))
        usedVariation = list(range(0, len(sentence.get("hanzi"))))
        print(usedVariation)
        for i in range(len(sentence.get("hanzi"))):
            variateX = rand.randint(0, 50)
            variateY = rand.randint(0, 200)
            placement = usedVariation.pop(
                rand.randrange(len(usedVariation)))
            print(placement)
            print(usedVariation)
            singleNode = {"id": "", "type": "customNode",
                          "data": {}, "position": {}, "width": 70, "height": 70}
            singleNode["id"] = i+1
            singleNode["data"] = {0: sentence.get("hanzi")[i]}
            singleNode["position"] = {
                "x": 100+(placement*70)+variateX, "y": 200+variateY}
            print('Hanzi: '+sentence.get("hanzi")
                  [i]+", X: "+str(variateX)+" Y: "+str(variateY)+", singleNode: "+str(singleNode))
            arrOfNodeData.append(singleNode)
        print(arrOfNodeData)
    return arrOfNodeData


def get_sentences(word, userLevel):
    print()
    print("Inside GetSentence")
    print("Here's the word we've selected: "+str(word))
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
    returnSentences = multipleChoicePick(sentencesContainingWord, 3)
    return returnSentences


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
