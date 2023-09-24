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
