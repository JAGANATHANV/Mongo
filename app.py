from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection URI
db = client['mydatabase']  # Replace with your database name
collection = db['mycollection']  # Replace with your collection name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'email': request.form['email'],
        }
        collection.insert_one(user_data)  # Insert data into MongoDB
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
