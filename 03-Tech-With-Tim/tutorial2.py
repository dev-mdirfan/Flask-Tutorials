# HTML Templates

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

'''
@app.route('/')
def home():
    return render_template("tutorial2/index.html")

@app.route('/user/<name>')
def user(name):
    return f"<h1>Hello, {name}</h1>"

@app.route('/admin')
def admin():
    return redirect(url_for('user', name="Admin!"))

@app.route('/<name>')
def home(name):
    return render_template("tutorial2/index.html", content=name)
'''

@app.route('/user/<name>')
def home(name):
    names = ["Tim", "Joe", "Bill"]
    return render_template("tutorial2/index.html", content=names, name=name)

@app.route('/status')
def status():
    status = "active"
    return render_template('tutorial2/status.html', content=status)

if __name__ == "__main__":
    app.run(debug=True)
