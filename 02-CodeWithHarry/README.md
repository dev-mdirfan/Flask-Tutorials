# 02. CodeWithHarry - Python Flask Web Development Tutorial in Hindi

## Installation

```bash
# Virtual Environment
python -m venv venv

# Activate Virtual Environment
venv\Scripts\activate

# Install Flask
pip install flask flask_sqlalchemy gunicorn
```

## Deploy on Heroku

- Install Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli)

```bash
# Login to Heroku
heroku login

# Create Heroku App
heroku create todo

# Add Git Remote
heroku git:remote -a todo

# Push to Heroku
git push heroku master

# Open Heroku App
heroku open
```

