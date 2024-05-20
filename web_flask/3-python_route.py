#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello as main page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb as a secondary page"""
    return 'HBNB'


@app.route('/c/<text>')
def c_param(text):
    """display C followed by value of text"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/<text>')
def python_param(text='is cool'):
    """display Python followed by value of text"""
    return 'Python {}'.format(text).replace('_', ' ')


if __name__ == "__main__":
    app.run()
