from flask import Flask

# This sets up the application using the Flask object from the package flask.
app = Flask(__name__)

# Using decorators the route is associated with the following method.
@app.route('/')
def hello():
    return 'Greetings sire, the Docker universe awaits you!'

@app.route('/welcome', defaults={'name': ''})
@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome to this awesome page %s!' % name

# This statement evaluates to true if this is the main python file. It starts up the Flask app on localhost with the default port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# $ export FLASK_APP=E3.py
# $ flask run
