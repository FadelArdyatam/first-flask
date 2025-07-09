from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# contoh data
books = [
    {"id": 1, "title": "Python for Beginners", "author": "John Doe"},
    {"id": 2, "title": "Flask API Guide", "author": "Jane Smith"}
]

# endpoint flask
@app.route('/')
def index():
    return "Welcome to the Flask API!"

@app.route('/api/books', methods=['GET'])
def getBooks():
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def addBook():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify({'message': 'new book added'}), 201

if __name__ == "__main__":
    app.run(debug=True)
    
    