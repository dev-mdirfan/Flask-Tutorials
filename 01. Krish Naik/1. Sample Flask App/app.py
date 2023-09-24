# 1. Sample Flask App
from flask import Flask

# This is WSGI application which is used to run the application
app = Flask(__name__)

# This is the route decorator which is used to bind the URL to the function
@app.route('/') # It has two arguments, first is the Rule (URL - str) and second is the Options: methods, default is GET (GET, POST, PUT, DELETE, etc)
def welcome():    # Binding function
    '''
    This is Home Page
    '''
    
    urls = """
        <html>
            <body>
                <h1> Welcome to Flask App! </h1> <br>
                <p> Go To <a href="/members">Members Page</a> </p>
            </body>
        </html>
        """
    # return "Hello World"
    return urls

@app.route('/members')
def members():
    return "Hello, Members <br> Welcome to Members Page."

if __name__ == "__main__":
    # app.run() has 4 parameters - host, port, debug, options
    # Example: app.run(host='hostname', port=5000, debug=True, options)
    app.run(debug=True)
    
    # debug=True - it will show the error on the browser and restart the server automatically
    # debug=False - it will not show the error on the browser and does not restart the server automatically
    
    # Run the application using the below command:
    # python app.py
    # or
    # flask run
