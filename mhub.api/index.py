from config import configuration
from apis import google
from flask import Flask
app = Flask(__name__)

import pprint
@app.route("/")
def index():
    #pprint.pprint(google.Google().search_youtube('michael jackson'))
    return "This is mhub api home!"


@app.route("/search/<q>")
def search(q):
    return "Your search word is " + q