# Code 1 - Routing and App Structure | Student Marks

- Routing is used to map the URL to the function.
- We can use `app.route()` decorator to bind the URL to the function.
- We can use `methods` parameter to specify the HTTP methods that should be handled by the function.
- We can use `app.add_url_rule()` to bind the URL to the function.

### Routing

```python
@app.route('/members')
def members():
    return "Hello, Members"
```

### Structure



```bash
# write the below code in app.py file
from flask import Flask

# WSGI Application
app = Flask(__name__)


# decorator - it runs below function when we hit the URL
@app.route('/')             # it has 2 parameters - URL (str) and method (GET, POST, PUT, DELETE, etc.)
def welcome():              # binding function
    return "Welcome to Flask!"

@app.route('/members')
def members():
    return "Hello, Members"

# it calls the main function and runs the application
if __name__ == '__main__':
    # it has 4 parameters - host, port, debug, options
    app.run(debug=True)    # debug=True - it will show the error on the browser
```

- Run the application using `python app.py`
- Paste the URL in the browser - `http://localhost:5000/` or `http://127.0.0.1:5000/`

- Go to file [app.py](../codes-1/app.py) for the code.

