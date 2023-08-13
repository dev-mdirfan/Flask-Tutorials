# Codes - 3 - Templates and HTTP Methods | Student Marks


- We can use `render_template()` function to render the HTML templates.
- We can use `request` object to get the data from the form.
- Template uses `Jinja2` template engine.

### Template

- Jinja2 is a template engine for Python.
- It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request.
- It can be used to generate any text-based format (HTML, XML, CSV, etc.).
- It is used to load dynamic data into HTML.
- It is used to create HTML templates with static and dynamic data and control the flow of the template and also to create macros and inherit templates and also to create filters and also to create tests and also to create namespaces and also to create extensions and also to create internationalization.

### `app.py`

```python
### Integrate with HTML With Flask
### HTTP verb GET and POST

# write the below code in main.py file
from flask import Flask, redirect, url_for, render_template, request

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:marks>/<string:result>/')
def success(marks, result):
    return render_template('result.html', marks=marks, result=result)

@app.route('/fail/<int:marks>/<string:result>/')
def fail(marks, result):
    return render_template('result.html', marks=marks, result=result)

# Result Checker
@app.route('/results/<int:marks>/')
def results(marks):
    result = ""
    if 0 < marks < 50:
        result = "Failed"
        return redirect(url_for('fail', marks=marks, result=result))
    elif 50 <= marks <= 100 :
        result = "Passed"
        return redirect(url_for('success', marks=marks, result=result))
    return render_template('Result can not be determined!')

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

- Go to file [main.py](codes/main.py) for the code.

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
