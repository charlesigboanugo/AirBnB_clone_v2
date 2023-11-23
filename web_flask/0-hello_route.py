#!/usr/bin/python3
"""The / route"""


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_route():
        """root folder route"""
        return "Hello HBNB!"

    app.run(host='0.0.0.0')
