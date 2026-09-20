#!/usr/bin/env python3
"""Flask app whose locale can be forced with a URL parameter.
"""
from typing import Optional

from flask import Flask, render_template, request
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
babel = Babel()


def get_locale() -> Optional[str]:
    """Return the locale forced by the locale URL parameter if it is
    supported, else the supported language that best matches the ones
    accepted by the request.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> str:
    """GET /
    Return: the home page
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
