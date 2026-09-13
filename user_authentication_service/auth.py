#!/usr/bin/env python3
"""Auth module: registers the users of the authentication service and
manages their passwords, sessions and reset password tokens.
"""
import uuid
from typing import Optional

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Return the salted bcrypt hash of the given password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return the string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        """Initialize a new Auth instance and its database.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password, and
        return it.

        Raise ValueError if a user is already registered with this email.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """Return True if the password is the one of the user registered
        with the given email, False otherwise.
        """
        if email is None or password is None:
            return False
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode("utf-8"), user.hashed_password)

    def create_session(self, email: str) -> Optional[str]:
        """Create a new session for the user registered with the given email
        and return its session ID, or None if no user has this email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """Return the user owning the given session ID, or None if the
        session ID is None or no user owns it.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session of the user with the given id by setting its
        session ID to None.
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for the user registered with the
        given email, save it and return it.

        Raise ValueError if no user is registered with this email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError("User {} does not exist".format(email))
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Set the password of the user owning the given reset token and
        invalidate the token.

        Raise ValueError if no user owns the reset token.
        """
        # A None token would match every user without a pending reset
        if reset_token is None:
            raise ValueError("Invalid reset token")
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError("Invalid reset token")
        self._db.update_user(user.id,
                             hashed_password=_hash_password(password),
                             reset_token=None)
