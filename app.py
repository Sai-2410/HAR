from flask import Flask, request, render_template, session, redirect, url_for, jsonify
import sqlite3
import secrets
import os
import subprocess
from data_collection import collection
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


connection = sqlite3.connect('database.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user (Id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, phone TEXT, email TEXT, password TEXT)"""
cursor.execute(command)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        email = request.form['email']
        password = request.form['password']

        query = "SELECT * FROM user WHERE email = '"+email+"' AND password= '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            session['user'] = result
            return render_template("home.html")
        else:
            return render_template("login.html")        
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        cursor.execute("INSERT INTO user VALUES (NULL, '"+fname+"', '"+lname+"', '"+phone+"', '"+email+"', '"+password+"')")
        connection.commit()

        return render_template("login.html")
    return render_template("login.html")


@app.route("/start", methods=['GET', 'POST'])
def start():
        in1 = request.form['in1']   
        print(in1)
        collection(in1)
        return render_template("home.html")


@app.route("/train", methods=['GET', 'POST'])
def train():
    subprocess.Popen(['start', 'cmd', '/k', 'python data_training.py'], shell=True)
    return render_template("home.html")

@app.route("/recognition", methods=['GET', 'POST'])
def recognition():
    subprocess.Popen(['start', 'cmd', '/k', 'python inference.py'], shell=True)
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
