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



