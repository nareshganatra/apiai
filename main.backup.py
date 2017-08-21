from flask import Flask
from flask import request
from flask import make_response
import json
import logging as l

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print "there u go"
    return 'Hello my Beaturiful World!\n'


@app.route('/apiai', methods=['POST'])
def yello():
    """Return a friendly HTTP greeting."""
    l.info("11")
    #print "1"
    speech = "This is a reponse from GAE !!"
    #print "2"
    l.info("22")
    my_response = {
     "speech" : speech,
     "displayText " : speech,
    } 
    l.info("33")
    #print "3"
    res = json.dumps(my_response)
    l.info("44")
    #print "4"
    r = make_response(res)
    l.info("55")
    #print "5"
    #print r
    #print type(r)
    r.headers['Content-Type'] = 'application/json'
    l.info("66")
    #print  type(r)
    #print "5"
    l.info("77")
    return r


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
