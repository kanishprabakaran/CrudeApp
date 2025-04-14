from flask import Flask, render_template, request, redirect, url_for
import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Firebase configuration using environment variables
firebaseConfig = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID")
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

@app.route('/')
def index():
    data = db.child("users").get().val()
    return render_template("form.html", users=data)

@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    email = request.form['email']
    user_data = {"name": name, "email": email}
    db.child("users").push(user_data)
    return redirect(url_for('index'))

@app.route('/update/<user_id>', methods=['POST'])
def update(user_id):
    name = request.form['name']
    email = request.form['email']
    db.child("users").child(user_id).update({"name": name, "email": email})
    return redirect(url_for('index'))

@app.route('/delete/<user_id>')
def delete(user_id):
    db.child("users").child(user_id).remove()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
