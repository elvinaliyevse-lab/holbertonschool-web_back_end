#!/usr/bin/env python3
"""Flask app using the locale of the logged in user.
"""
from typing import Dict, Optional

from flask import Flask, g, render_template, request
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> Optional[str]:
    """Return the first supported locale among the one forced by the
    locale URL parameter, the one of the logged in user and the ones
    accepted by the request.
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    user = getattr(g, "user", None)
    if user is not None and user["locale"] in app.config["LANGUAGES"]:
        return user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


def get_user() -> Optional[Dict[str, Optional[str]]]:
    """Return the user whose ID is given by the login_as URL parameter,
    or None if the parameter is missing or does not match any user.
    """
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    try:
        return users.get(int(login_as))
    except ValueError:
        return None


@app.before_request
def before_request() -> None:
    """Set the logged in user, if any, as a global of the request."""
    g.user = get_user()


@app.route("/", strict_slashes=False)
def index() -> str:
    """GET /
    Return: the home page
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
