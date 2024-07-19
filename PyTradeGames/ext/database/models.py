"""Implementation of the Database Models"""

from . import db

from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey, Column, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


class Users(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String(255), nullable=False)
    country:Mapped[str] = mapped_column(String(255), nullable=False)
    # games

    def __repr__(self) -> str:
        return f'User(id={self.id}, username={self.username})'


class Games(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # genre
    # console
    # users


class Genres(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    genre:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    # games
    

class Consoles(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    manufacturer:Mapped[str] = mapped_column(String(255), nullable=False)
    # games
    

class Messages(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    content:Mapped[str] = mapped_column(String(255), nullable=False)
    status:Mapped[bool] = mapped_column(nullable=False)
    # sender
    # receiver
    # game
    

class Review(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    grade:Mapped[int] = mapped_column(CheckConstraint('grade > 0 AND grade < 6'), nullable=False)
    message:Mapped[Optional[str]] = mapped_column(String(255))
    # user_reviewer
    # user_reviewed
    