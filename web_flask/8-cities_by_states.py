#!/usr/bin/python3
"""The / route"""

if __name__ == "__main__":
    from models import storage
    from models.state import State
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/cities_by_states/', strict_slashes=False)
    def states_list():
        """list states from database"""
        return flask.render_template('8-cities_by_states.html',
                                     states=storage.all(State))

    app.run(host='0.0.0.0')

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        storage.close()
