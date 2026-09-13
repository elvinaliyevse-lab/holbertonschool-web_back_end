# User authentication service

A user authentication service built with Flask, SQLAlchemy and bcrypt.

In the industry, you should not implement your own authentication system but
use a module or framework doing it for you (like
[Flask-User](https://flask-user.readthedocs.io/en/latest/) for Flask). Here,
for learning purposes, each step of the mechanism is implemented from scratch.

## Learning objectives

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Files

- `user.py`: `User` SQLAlchemy model, mapped to the `users` table
- `db.py`: `DB` class, to add, find and update users in the database
- `auth.py`: `Auth` class, to register users, validate their credentials and manage their sessions and reset password tokens
- `app.py`: Flask app exposing the end-points of the service

## Setup

```
$ pip3 install bcrypt flask sqlalchemy
```

## Run

```
$ python3 app.py
```

The app listens on `0.0.0.0:5000`. Users are stored in the SQLite database
`a.db`, which is reset every time the app starts.

## Routes

- `GET /`: returns a welcome message
- `POST /users`: registers a user (form data: `email`, `password`)
- `POST /sessions`: logs a user in (form data: `email`, `password`) and sets the `session_id` cookie
- `DELETE /sessions`: logs out the user of the `session_id` cookie and redirects to `GET /`
- `GET /profile`: returns the email of the user of the `session_id` cookie
- `POST /reset_password`: generates a reset password token (form data: `email`)
- `PUT /reset_password`: updates a password with a reset password token (form data: `email`, `reset_token`, `new_password`)
