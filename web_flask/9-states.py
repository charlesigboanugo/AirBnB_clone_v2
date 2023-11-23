#!/usr/bin/python3
"""The / route"""

if __name__ == "__main__":
    from models import storage
    from models.state import State
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/states/', defaults={"id": None}, strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def states_list(id):
        """list states from database"""
        validid = 0
        states = storage.all(State).values()
        if id is None:
            validid = 1
        else:
            for state in states:
                if id == state.id:
                    validid = 1
                    break
        return flask.render_template('9-states.html', idnum=id,
                                     states=storage.all(State),
                                     validid=validid)

    app.run(host='0.0.0.0')

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        storage.close()
