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



