#!/usr/bin/python3
"""
representes one function that make route to '/'
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
