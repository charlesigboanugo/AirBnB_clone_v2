#!/usr/bin/python3
"""The / route"""


if __name__ == "__main__":
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """root folder route"""
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb_route():
        """/hbnb/ folder route"""
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def c_route(text):
        """output some text depending on url after /c/"""
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/<text>', strict_slashes=False)
    def python_route(text):
        """output some text depending on url after /python/"""
        return "Python " + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def number_route(n):
        """output some number depending on url after /number/"""
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_template(n):
        """output some number depending on url after /number_template/"""
        return flask.render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_odd_or_even(n):
        """output some number and odd/even"""
        if n % 2 == 0:
            evenodd = "even"
        else:
            evenodd = "odd"
        return flask.render_template('6-number_odd_or_even.html', n=n,
                                     evenodd=evenodd)

    app.run(host='0.0.0.0')
