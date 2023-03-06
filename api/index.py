from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/<name>')
def about(name):
    return jsonify({'message': f'Hello{name}'})


@app.route('/about')
def about():
    return jsonify({'message': 'Hello from serverless Flask!'})


if __name__ == '__main__':
    app.run(debug=True)
