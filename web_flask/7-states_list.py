#!/usr/bin/python3
"""
represents /states_list route logic
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """return all State objects in the database"""
    states_objects_vals = storage.all(State).values()
    return render_template(
        "7-states_list.html",
        states_objects=sorted(states_objects_vals, key=lambda x: x.name),
    )


@app.teardown_appcontext
def db_close_connection(exception=None):
    """close database connection at the end of context"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
