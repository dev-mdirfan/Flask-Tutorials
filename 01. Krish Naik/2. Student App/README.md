# Student Marks Checker App

- We can bind the URL dynamically using `<variable_name>` in the URL.
- We can use `url_for()` function to generate the URL dynamically for the given function.

## Tutorial

```python
# 2. Student App
# Learn: Binding URL Dynamically and Variable Rules

from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    urls = """
    <html>
        <body>
            <h1> Welcome to Flask! </h1> <br>
            <p> <a href="/success/70"> Success </a> <strong>Write on url:</strong> /success/55 </p>
            <p> <a href="/fail/20"> Fail </a> <strong>Write on url:</strong> /fail/55 </p>
            <p> <a href="/results/50"> Results </a> <strong>Write on url:</strong> /results/40 or /results/60 </p>
        </body>
    </html>
    """
    return urls

# Dynamic URL
@app.route('/success/<int:score>/')
def success(score):
    '''
    This page will show the result of the student
    '''
    return f"<html><body><h1> The person has passed and the marks is {score}.</h1></body></html>"

@app.route('/fail/<int:score>/')
def fail(score):
    return f"<html><body><h1> The person has failed and the marks is {score} </h1></body></html>"

# Result Checker
@app.route('/results/<int:score>/')
def results(score):
    result = ""
    if score < 50:
        result = "fail"
    else:
        result = "success"
    # return result
    return f"<html><body><h1> The person has {result} and the marks is {score} </h1></body></html>"

if __name__ == "__main__":
    app.run(debug=True)

```


### Note: for using different - 2 pages we use url_for() method

```python
# 2. Student App 2
# Learn: Binding URL Dynamically and Variable Rules

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    urls = """
    <html>
        <body>
            <h1> Welcome to Flask! </h1> <br>
            <p> <a href="/success/70"> Success </a> <strong>Write on url:</strong> /success/55 </p>
            <p> <a href="/fail/20"> Fail </a> <strong>Write on url:</strong> /fail/55 </p>
            <p> <a href="/results/50"> Results </a> <strong>Write on url:</strong> /results/40 or /results/60 </p>
        </body>
    </html>
    """
    return urls

# Dynamic URL
@app.route('/success/<int:score>/')
def success(score):
    '''
    This page will show the result of the student
    '''
    return f"<html><body><h1> The person has passed and the marks is {score}.</h1></body></html>"

@app.route('/fail/<int:score>/')
def fail(score):
    return f"<html><body><h1> The person has failed and the marks is {score} </h1></body></html>"

# Result Checker
@app.route('/results/<int:score>/')
def results(score):
    result = ""
    if score < 50:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score = score))    # it will redirect to the URL of the function

if __name__ == "__main__":
    app.run(debug=True)
```