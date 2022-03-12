from flask import Flask
import requests

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

@app.route('/weather/<city>')
def weather(city):
    request = 'https://www.metaweather.com/api/location/search/?query=%s' % city
    data = get_data_from_url_request(request)
    woeid = data[0]['woeid']
    request = 'https://www.metaweather.com/api/location/%s/' % woeid
    data = get_data_from_url_request(request)
    temp = data['consolidated_weather'][0]['the_temp']
    return 'The temperature in %s is: %s' % (city, temp)

def get_data_from_url_request(url_endpoint):
    response = requests.get(url_endpoint)                   # get url response
    data = response.json()                                  # read it as json
    return data

# This statement evaluates to true if this is the main python file. It starts up the Flask app on localhost with the default port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# $ export FLASK_APP=E5.py
# $ flask run
