from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World </h1>"


@app.route("/about")
def about():
    me = {
        "first_name": "Daniel",
        "last_name": "Avilez",
        "hobby": "Collecting shoes, and cars"


    }
    return me
