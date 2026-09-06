# Session authentication

Continuation of the `Basic authentication` project: the API is now protected by
a Session Authentication mechanism, implemented from scratch (for learning
purposes — in production you should use an already established module or
framework).

## Learning objectives

- What authentication means
- What session authentication means
- What cookies are
- How to send cookies
- How to parse cookies

## Files

### `models/`

- `base.py`: base of all models of the API — handles serialization to file
- `user.py`: user model
- `user_session.py`: session model, to store Session IDs in the database

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints, including `GET /users/me`
- `views/session_auth.py`: login and logout endpoints
- `auth/auth.py`: base of all authentication systems
- `auth/basic_auth.py`: Basic authentication
- `auth/session_auth.py`: Session authentication (in memory)
- `auth/session_exp_auth.py`: Session authentication with an expiration date
- `auth/session_db_auth.py`: Session authentication stored in the database

## Setup

```
$ pip3 install -r requirements.txt
```

## Run

The authentication system is selected with the `AUTH_TYPE` environment
variable: `auth`, `basic_auth`, `session_auth`, `session_exp_auth` or
`session_db_auth`.

```
$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth \
  SESSION_NAME=_my_session_id python3 -m api.v1.app
```

`SESSION_NAME` defines the name of the cookie holding the Session ID, and
`SESSION_DURATION` (in seconds) the lifetime of a session for
`session_exp_auth` and `session_db_auth`.

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `POST /api/v1/auth_session/login`: logs a user in (form parameters: `email`, `password`) and sets the session cookie
- `DELETE /api/v1/auth_session/logout`: logs the current user out
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID — `me` returns the authenticated user
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
