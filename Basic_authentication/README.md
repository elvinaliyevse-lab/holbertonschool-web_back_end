# Basic authentication

Simple HTTP API for playing with a `User` model, on top of which a Basic
Authentication mechanism is implemented (for learning purposes — in production
you should use an already established module or framework).

## Learning objectives

- What authentication means
- What Base64 is and how to encode a string in Base64
- What Basic authentication means
- How to send the `Authorization` header

## Files

### `models/`

- `base.py`: base of all models of the API — handles serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

## Requirements

- Ubuntu 18.04 LTS, Python 3.7
- All files end with a new line and are executable
- Code follows `pycodestyle` (version 2.5)
- All modules, classes and functions are documented

## Setup

```
$ pip3 install -r requirements.txt
```

## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
