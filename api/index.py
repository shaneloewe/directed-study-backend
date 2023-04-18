from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from queries import *
from dbInsert import update_progress, db_insert, add_to_incorrect
import config
from urllib.parse import unquote

# The user data is going to be stored in a database
# For any given page, we want to be able to access the
# necessary user information that the page needs.


app = Flask(__name__)
CORS(app)

# Called in: Home page

currentUser = None


@app.route('/<userEmail>')
def home(userEmail):
    # Check to see if Email exists in database
    # print("This is our Database:")
    # print(return_all())
    # print()
    # print("This is the userEmail we got passed: "+str(userEmail))
    userStatus = get_userid(str(userEmail))
    # print("Just ran the get_userId Function")
    # print("User Status: "+str(userStatus))
    if userStatus == False:
        # print("User not found. Adding user to Database?")
        db_insert(str(userEmail))

    return ""

    # data = {'userId': user_id}
    # print("DATA!: "+data['userId'])
    # return json.dumps(data)


@app.route('/dictionary/<userEmail>')
def getDict(userEmail):
    userDict = get_userdict(str(userEmail))
    for item in userDict:
        print(item)
    return jsonify({'dictionary': userDict})

    # data = {'userId': user_id}
    # print("DATA!: "+data['userId'])
    # return json.dumps(data)


@app.route('/profile/<userEmail>')
def getStats(userEmail):
    userStats = get_profile_stats(str(userEmail))
    for item in userStats:
        print(item)
    return jsonify({'stats': userStats})


@app.route('/sentence/<userEmail>')
def getSentence(userEmail):
    userLevel = get_userLevel(str(userEmail))
    word = get_word(userLevel)
    sentences = get_sentences(word, userLevel)
    packagedSentences = multipleChoicePick(sentences, 3)
    # print(type(sentences))
    print("This is the sentence Dictionary: "+str(packagedSentences))
    print("Type of 'sentences': "+str(type(packagedSentences)))
    for sentence in packagedSentences:
        print(str(sentence))
    return jsonify({'sentences': packagedSentences, 'word': word})

    # data = {'userId': user_id}
    # print("DATA!: "+data['userId'])
    # return json.dumps(data)

# Called in: About page


@app.route('/correct_answer')
def correctAnswer():
    userEmail = request.args.get('userEmail')
    word = unquote(request.args.get('word'))
    print(userEmail)
    print(word)
    update_progress(userEmail, word)
    return ""


@app.route('/incorrect_answer/<userEmail>')
def incorrectAnswer(userEmail):
    print(userEmail)
    add_to_incorrect(userEmail)
    return ""


@app.route('/builder/<userEmail>')
def sentenceBuilder(userEmail):
    userLevel = get_userLevel(str(userEmail))
    word = get_word(userLevel)
    sentences = get_sentences(word, userLevel)
    packagedSentences = multipleChoicePick(sentences, 1)
    # Now split the sentence into a bunch of words
    arrOfNodes = splitSentence(packagedSentences)
    wordList = return_all()
    return jsonify({'sentence': packagedSentences, 'nodes': arrOfNodes, 'word': word, 'words': wordList})


@app.route('/isWord/<word>')
def isWord(word):
    foundWord = check_word(word)
    return jsonify({'foundWord': foundWord})


@app.route('/about')
def about():
    return jsonify({'message': 'Hello from serverless Flask!'})


if __name__ == '__main__':
    app.run
