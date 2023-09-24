# 3. Student Marks Checker App with Templates

- We can use `render_template()` function to render the HTML templates.
- We can use `request` object to get the data from the form.
- Template uses `Jinja2` template engine.

## Template

- Jinja2 is a template engine for Python.
- It is used to create HTML, XML or other markup formats that are returned to the user via an HTTP request.
- It can be used to generate any text-based format (HTML, XML, CSV, etc.).
- It is used to load dynamic data into HTML.
- It is used to create HTML templates with static and dynamic data and control the flow of the template and also to create macros and inherit templates and also to create filters and also to create tests and also to create namespaces and also to create extensions and also to create internationalization.

## Tutorial

```python
# 3. Student App with Templates
# Learn: 1. How to use templates in Flask (Integrate with HTML With Flask)
# Learn: 2. Different types of request methods (HTTP verb GET and POST)

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result Checker - GET and POST of HTML Form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        english = float(request.form['English'])
        c = float(request.form['C'])
        data_science = float(request.form['DataScience'])
        total_score = science + maths + english + c + data_science
        avg = total_score / 5
    else:
        return '<h1>Error Occurred</h1>'
    result = ""
    url = ""
    if 0 < avg < 50:
        url = "fail"
        result = "Failed"
    elif 50 <= avg <= 100 :
        url = "success"
        result = "Passed"
    return redirect(url_for(url, marks = avg, result = result))

@app.route('/success/<int:marks>/<string:result>/')
def success(marks, result):
    return render_template('result.html', marks=marks, result=result)

@app.route('/fail/<int:marks>/<string:result>/')
def fail(marks, result):
    return render_template('result.html', marks=marks, result=result)

if __name__ == '__main__':
    app.run(debug=True)
```

### Different - 2 routes for results, success and fail

```python
# 3. Student App with Templates
# Learn: 1. How to use templates in Flask (Integrate with HTML With Flask)
# Learn: 2. Different types of request methods (HTTP verb GET and POST)

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result Checker - GET and POST of HTML Form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        english = float(request.form['English'])
        c = float(request.form['C'])
        data_science = float(request.form['DataScience'])
        total_score = science + maths + english + c + data_science
        avg = total_score / 5
        return redirect(url_for('results', marks=avg))
    else:
        return 'Error Occurred'

# Result Checker - for success and fail
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

@app.route('/success/<int:marks>/<string:result>/')
def success(marks, result):
    return render_template('result.html', marks=marks, result=result)

@app.route('/fail/<int:marks>/<string:result>/')
def fail(marks, result):
    return render_template('result.html', marks=marks, result=result)

if __name__ == '__main__':
    app.run(debug=True)
```

### Single route for results, success and fail

```python
# 3. Student App with Templates
# Learn: 1. How to use templates in Flask (Integrate with HTML With Flask)
# Learn: 2. Different types of request methods (HTTP verb GET and POST)

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result Checker - GET and POST of HTML Form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        english = float(request.form['English'])
        c = float(request.form['C'])
        data_science = float(request.form['DataScience'])
        total_score = science + maths + english + c + data_science
        avg = total_score / 5
        return redirect(url_for('results', marks=avg))
    else:
        return 'Error Occurred'

# Result Checker - for success and fail
@app.route('/results/<int:marks>')
def results(marks):
    if 0 <= marks < 50:
        result = "Failed"
        return render_template('result.html', marks=marks, result=result)
    elif 50 <= marks <= 100 :
        result = "Passed"
        return render_template('result.html', marks=marks, result=result)
    else:
        result = "Result is out of 0 - 100"
    return render_template('result.html', marks=marks, result=result)

if __name__ == '__main__':
    app.run(debug=True)
```
