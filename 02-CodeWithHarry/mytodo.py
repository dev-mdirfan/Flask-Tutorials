from flask import Flask, render_template, request, session, redirect
# flask-sqlalchemy is an ORM (Object Relational Mapper) which provides a mapping between Object and Relational Databases.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# @app.route('/')
# def hello_world():
    # return 'Hello, World!'
    
    # How to add data to database
    # todo = Todo(title='Buy Milk', desc='Milk is good')
    # db.session.add(todo)
    # db.session.commit()
    
    # How to read all data from database
    # allTodo = Todo.query.all()
    # return render_template('index.html', allTodo = allTodo)


# @app.route('/show')
# def show():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return 'This is Show page'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # print('POST')
        # print(request.form) # list of all the data in the form in ImmutableMultiDict format
        title = request.form['title']
        desc = request.form['desc']
        
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        # Method 1
        '''
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        '''
        # Method 2
        todo = Todo.query.filter_by(sno = sno).update(dict(title = title, desc = desc))
        db.session.commit()
        return redirect('/')
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo = todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)



# To create a database in python shell:
'''
> from app import app, db
> app.app_context().push()
> db.create_all()
> exit()
'''