# How to Make Website with Python

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, this is the main page</h1>"

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}</h1>"

@app.route('/admin')
def admin():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)