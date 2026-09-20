#!/usr/bin/env python3
"""Basic Flask app with a single route rendering a home page.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index() -> str:
    """GET /
    Return: the home page
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
