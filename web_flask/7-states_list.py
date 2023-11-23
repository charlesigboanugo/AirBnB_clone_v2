#!/usr/bin/python3
"""The / route"""

if __name__ == "__main__":
    from models import storage
    from models.state import State
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/states_list/', strict_slashes=False)
    def states_list():
        """list states from database"""
        statedict = storage.all(State)
        return flask.render_template('7-states_list.html', states=statedict)

    app.run(host='0.0.0.0', port=5000)

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        storage.close()
