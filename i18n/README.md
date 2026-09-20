# i18n

Internationalization of a Flask app with Flask-Babel: translated templates,
locale inferred from the URL, the logged in user and the request headers,
and a localized display of the current time.

## Learning objectives

- How to parametrize Flask templates to display different languages
- How to infer the correct locale based on URL parameters, user settings or
  request headers
- How to localize timestamps

## Files

- `0-app.py`: basic Flask app with a single `/` route
- `1-app.py`: `Config` class setting the available languages, and the default
  locale and timezone of Babel
- `2-app.py`: `get_locale`, matching the languages accepted by the request
- `3-app.py`: templates parametrized with `gettext`
- `4-app.py`: locale forced with the `locale` URL parameter
- `5-app.py`: login mocked with the `login_as` URL parameter
- `6-app.py`: locale of the logged in user
- `7-app.py`: `get_timezone`, validated with `pytz`
- `app.py`: current time, displayed in the timezone of the user
- `babel.cfg`: files Babel extracts the messages from
- `templates/`: one template per task
- `translations/`: English and French message catalogs

## Setup

```
$ pip3 install flask flask_babel pytz
```

## Usage

```
$ python3 app.py
```

Then visit `http://127.0.0.1:5000/`, optionally with the `locale`, `login_as`
and `timezone` URL parameters, for instance
`http://127.0.0.1:5000/?login_as=1&timezone=Europe/London`.

## Translations

The catalogs are extracted, initialized and compiled with:

```
$ pybabel extract -F babel.cfg -o messages.pot .
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
$ pybabel compile -d translations
```
