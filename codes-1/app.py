# write the below code in app.py file
from flask import Flask, redirect, url_for

# WSGI Application
app = Flask(__name__)


# decorator - it runs below function when we hit the URL
@app.route('/')             # it has 2 parameters - URL (str) and method (GET, POST, PUT, DELETE, etc.)
def welcome():              # binding function
    urls = """
    <html>
        <body>
            <h1> Welcome to Flask! </h1> <br>
            <a href="/members"> Members </a> <br>
            <a href="/success/70"> Success </a> <br>
            <a href="/fail/20"> Fail </a> <br>
            <a href="/results/50"> Results </a>
        </body>
    </html>
    """
    return urls

@app.route('/members')
def members():
    return "Hello, Members"

# Dynamic URL
@app.route('/success/<int:score>/')
def success(score):
    return "<html><body><h1> The person has passed and the marks is {} </h1></body></html>".format(score)

@app.route('/fail/<int:score>/')
def fail(score):
    return "<html><body><h1> The person has failed and the marks is {} </h1></body></html>".format(score)

# Result Checker
@app.route('/results/<int:marks>/')
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "success"
    # return "<html><body><h1> The person has {} and the marks is {} </h1></body></html>".format(result, marks)
    return redirect(url_for(result, score=marks))    # it will redirect to the URL of the function


# it calls the main function and runs the application
if __name__ == '__main__':
    # it has 4 parameters - host, port, debug, options
    app.run(debug=True)    # debug=True - it will show the error on the browser
