#!/usr/bin/env python3
"""DB module: stores the users of the authentication service with SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class, used to add, find and update users in the database.
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        # Flask serves each request in a new thread, and the memoized
        # session reuses its SQLite connection across requests
        self._engine = create_engine(
            "sqlite:///a.db", echo=False,
            connect_args={"check_same_thread": False})
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save a new user with the given email and hashed password to the
        database and return it.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
        return user

    def find_user_by(self, **kwargs) -> User:
        """Return the first user matching all the given keyword arguments.

        Raise NoResultFound if no user matches, and InvalidRequestError if
        an argument is not an attribute of User.
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the attributes of the user with the given id and commit
        the changes to the database.

        Raise ValueError, without updating anything, if an argument is not
        an attribute of User.
        """
        user = self.find_user_by(id=user_id)
        columns = User.__table__.columns.keys()
        for key in kwargs:
            if key not in columns:
                raise ValueError("User has no attribute {}".format(key))
        for key, value in kwargs.items():
            setattr(user, key, value)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
