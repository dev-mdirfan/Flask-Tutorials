# Codes - 4 Static Files and Request Object - [Code](../codes-4/) | [Docs](../docs/codes-4.md)


### `app.py`

```python
# write the below code in app.py file
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
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

```

### `main.py`

```python
### Integrate with HTML With Flask
### HTTP verb GET and POST

# write the below code in main.py file

'''
{%...%} - for statements
{{...}} - for expressions to print the value
{#...#} - for comments
{%...%} - if, for, while, switch, case, break, continue, etc.
'''

from flask import Flask, redirect, url_for, render_template, request
# from markupsafe import Markup

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result Checker
@app.route('/results/<int:marks>/')
def results(marks):
    result = ''
    if marks < 50:
        result = 'Fail'
    else:
        result = 'Pass'
    expression = {'result': result, 'marks': marks}
    return render_template('results.html', exp= expression)

# Result Checker - GET and POST
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        english = float(request.form['English'])
        c = float(request.form['C'])
        datascience = float(request.form['DataScience'])
        total_score = science + maths + english + c + datascience
        avg = total_score / 5
        return redirect(url_for('results', marks=avg))
    else:
        return 'Error Occurred'

if __name__ == '__main__':
    app.run(debug=True)
```
