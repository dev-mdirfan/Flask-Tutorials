# 4. Student App with Templates Part 2
# Learn:
'''
{%...%} - statements static/url
{%...%} - if, for, while, switch, case, break, continue, etc.
{{...}} - expressions to print the value
{#...#} - comments
'''

from flask import Flask, redirect, url_for, render_template, request
# from markupsafe import Markup


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result Checker
@app.route('/results/<int:marks>/')
def results(marks):
    result = ''
    if 0 <= marks < 50:
        result = 'FAIL'
    elif 50 <= marks <= 100:
        result = 'PASS'
    else:
        result = 'INVALID MARKS'
    expression = {'results': result, 'marks': marks}
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
        data_science = float(request.form['DataScience'])
        total_score = science + maths + english + c + data_science
        avg = total_score / 5
        return redirect(url_for('results', marks=avg))
    else:
        return 'Error Occurred'

if __name__ == '__main__':
    app.run(debug=True)
