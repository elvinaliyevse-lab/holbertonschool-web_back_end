#!/usr/bin/env python3
"""Flask app with Babel set up for English and French.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration of the available languages, and of the locale and
    the timezone Babel falls back to.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index() -> str:
    """GET /
    Return: the home page
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
