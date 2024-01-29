#!/usr/bin/python3
"""
represnets /hbnb_filters route logic
"""

from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main Hbnb filters"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception=None):
    """close the db connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
