from . import db

from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional


class Users(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'User(id={self.id}, username={self.username})'