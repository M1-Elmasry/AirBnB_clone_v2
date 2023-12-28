#!/usr/bin/python3
"""
representes some routes
listening on 0.0.0.0:5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    return the content of the '/' page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return the content of the '/hbnb' page
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    return the content of the '/c/<text>' page
    with 'C' followed by '<text>'
    if text has '_' will replace it with whitespace
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
