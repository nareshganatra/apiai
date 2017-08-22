from flask import Flask
from flask import request
from flask import make_response
import json
import logging as l

app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    l.info("reached the hello() module...")

    return 'Hello  Beautiful World!\n'


@app.route('/apiai', methods=['POST'])
def apiai_response():
    """Return a static message to api.ai."""
    """Naresh  Ganatra"""

    l.info("reached apaai_response module ...... ")

    speech = "This is a reponse from GAE !! " 

    my_response = {
     "speech" : speech,
     "displayText " : speech,
    } 

    res = json.dumps(my_response)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'

    l.info("Exiting the  apaai_response module ...... ")

    return r


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
