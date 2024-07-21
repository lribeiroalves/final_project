"""Implementation of the Database Models"""

from . import db

from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey, Column, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List


class UserGames(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('users.id'))
    game_id = Column('game_id', Integer(), ForeignKey('games.id'))


class GamesGenre(db.Model):
    id = Column(Integer(), primary_key=True)
    game_id = Column('game_id', Integer(), ForeignKey('games.id'))
    genre_id = Column('genre_id', Integer(), ForeignKey('genres.id'))


class GamesConsole(db.Model):
    id = Column(Integer(), primary_key=True)
    game_id = Column('game_id', Integer(), ForeignKey('games.id'))
    console_id = Column('console_id', Integer(), ForeignKey('consoles.id'))


class Users(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String(255), nullable=False)
    country:Mapped[str] = mapped_column(String(255), nullable=False)
    admin:Mapped[bool] = mapped_column(nullable=False, default=False)
    
    # relations
    games:Mapped[List['Games']] = relationship(secondary='user_games', back_populates='users')

    def __repr__(self) -> str:
        return f'User(id={self.id}, username={self.username})'


class Games(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    
    # relations
    users:Mapped[List['Users']] = relationship(secondary='user_games', back_populates='games')
    genres:Mapped[List['Genres']] = relationship(secondary='games_genre', back_populates='games')
    consoles:Mapped[List['Consoles']] = relationship(secondary='games_console', back_populates='games')

    def __repr__(self) -> str:
        return f'Game(id={self.id}, name={self.name}, genre={self.genres}, console={self.consoles})'


class Genres(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    genre:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

    # relations
    games:Mapped[List['Games']] = relationship(secondary='games_genre', back_populates='genres')

    def __repr__(self) -> str:
        return f'{self.genre}'


class Makers(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'{self.name}'
    

class Consoles(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    
    # relations
    games:Mapped[List['Games']] = relationship(secondary='games_console', back_populates='consoles')
    makers:Mapped[int] = mapped_column(ForeignKey('makers.id'))

    def __repr__(self) -> str:
        return f'{self.name}'
    

class Messages(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    content:Mapped[str] = mapped_column(String(255), nullable=False)
    status:Mapped[bool] = mapped_column(nullable=False)
    
    # relations
    from_user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    to_user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    game_id:Mapped[int] = mapped_column(ForeignKey('games.id'))
    

class Reviews(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    grade:Mapped[int] = mapped_column(CheckConstraint('grade > 0 AND grade < 6'), nullable=False)
    message:Mapped[Optional[str]] = mapped_column(String(255))
    
    # relations
    from_user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    to_user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    