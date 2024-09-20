"""Data to be used to populate the database on development"""

from PyTradeGames.ext.database import db
from PyTradeGames.ext.database.models import Users, Games, Genres, Maker, Consoles, Trades


def create_makers():    
    makers = [
        Maker(name = 'Sony'),
        Maker(name = 'Microsoft'),
        Maker(name = 'Nintendo'),
        Maker(name = 'Sega'),
        Maker(name = 'Atari'),
    ]


def create_consoles(makers_query:list):
    consoles = [
        Consoles(name = 'PlayStation - PS1', maker = makers_query[0]), # 0
        Consoles(name = 'PlayStation 2 - PS2', maker = makers_query[0]), # 1
        Consoles(name = 'PlayStation 3 - PS3', maker = makers_query[0]), # 2
        Consoles(name = 'PlayStation 4 - PS4', maker = makers_query[0]), # 3
        Consoles(name = 'PlayStation 5 - PS5', maker = makers_query[0]), # 4
        Consoles(name = 'XBOX', maker = makers_query[1]), # 5
        Consoles(name = 'XBOX 360', maker = makers_query[1]), # 6
        Consoles(name = 'XBOX ONE', maker = makers_query[1]), # 7
        Consoles(name = 'XBOX SERIES X/S', maker = makers_query[1]), # 8
        Consoles(name = 'Pong', maker = makers_query[4]), # 9
        Consoles(name = 'Color TV Game', maker = makers_query[2]), # 10
        Consoles(name = 'Atari 2600', maker = makers_query[4]), # 11
        Consoles(name = 'Atari 2600', maker = makers_query[4]), # 12
        Consoles(name = 'Atari 5200', maker = makers_query[4]), # 13
        Consoles(name = 'Atari 2800', maker = makers_query[4]), # 14
        Consoles(name = 'Atari 7800', maker = makers_query[4]), # 15
        Consoles(name = 'NES/Famicon', maker = makers_query[2]), # 16
        Consoles(name = 'Master System', maker = makers_query[3]), # 17
        Consoles(name = 'Game Boy', maker = makers_query[2]), # 18
        Consoles(name = 'Game Gear', maker = makers_query[3]), # 19
        Consoles(name = 'Mega Drive/Genesis', maker = makers_query[3]), # 20
        Consoles(name = 'Super Nintendo/Super Famicon', maker = makers_query[2]), # 21
        Consoles(name = '???', maker = makers_query[2]), # 22
        Consoles(name = 'Atari Jaguar', maker = makers_query[4]), # 23
        Consoles(name = 'Sega Saturn', maker = makers_query[3]), # 24
        Consoles(name = 'Sega Saturn', maker = makers_query[3]), # 25
        Consoles(name = 'Virtual Boy', maker = makers_query[2]), # 26
        Consoles(name = 'Nintendo 64', maker = makers_query[2]), # 27
        Consoles(name = 'Game Boy Color', maker = makers_query[2]), # 28
        Consoles(name = 'PocketStation', maker = makers_query[0]), # 29
        Consoles(name = 'Dreamcast', maker = makers_query[3]), # 30
        Consoles(name = 'Game Boy Advance', maker = makers_query[2]), # 31
        Consoles(name = 'Nintendo Game Cube', maker = makers_query[2]), # 32
        Consoles(name = 'Nintendo Game Cube', maker = makers_query[2]), # 33
        Consoles(name = 'Nintendo DS', maker = makers_query[2]), # 34
        Consoles(name = 'PSP', maker = makers_query[0]), # 35
        Consoles(name = 'Nintendo Wii', maker = makers_query[2]), # 36
        Consoles(name = 'Nintendo 3DS', maker = makers_query[2]), # 37
        Consoles(name = 'PlayStation Vita', maker = makers_query[0]), # 38
        Consoles(name = 'Nintendo Wii U', maker = makers_query[2]), # 39
        Consoles(name = 'Nintendo Wii U', maker = makers_query[2]), # 40
        Consoles(name = 'Nintendo Switch', maker = makers_query[2]), # 41
    ]


def create_genres():
    genres =[
        Genres(genre = 'Action-Adventure'), # 0
        Genres(genre = 'Survival Horror'), # 1
        Genres(genre = 'Metroidvania'), # 2
        Genres(genre = 'Puzzle'), # 3
        Genres(genre = 'RPG'), # 4
        Genres(genre = 'MMORPG'), # 5
        Genres(genre = 'Roguelike'), # 6
        Genres(genre = 'Simulation'), # 7
        Genres(genre = 'Real Time Strategy'), # 8
        Genres(genre = 'Tower Defense'), # 9
        Genres(genre = 'Racing'), # 10
        Genres(genre = 'Sports'), # 11
        Genres(genre = 'Shooter'), # 12
        Genres(genre = 'First Person Shooter'), # 13
        Genres(genre = 'War'), # 14
        Genres(genre = 'Fighting'), # 15
        Genres(genre = 'Arcade'), # 16
    ]


def create_games(genres=[], consoles=[]):
    games = [
        Games(name='007: The World Is Not Enough', genres = [genres[0], genres[12]], consoles = [consoles[0]]),
        Games(name='Ace Combat 2', genres = [genres[14], genres[12]], consoles = [consoles[0]]),
        Games(name='Ace Combat 3: Electrosphere', genres = [genres[14], genres[12]], consoles = [consoles[0]]),
        Games(name='All Star Tennis "99"', genres = [genres[11]], consoles = [consoles[0], consoles[27], consoles[28]]),
        Games(name='Batman & Robin', genres=[genres[0], genres[15]], consoles=[consoles[0]]),
        Games(name='Bomberman Wars', genres=[genres[0], genres[8]], consoles=[consoles[0], consoles[24]]),
        Games(name='Castlevania: Symphony of the Night', genres=[genres[0], genres[2]], consoles=[consoles[0], consoles[24], consoles[6], consoles[35], consoles[3]]),
        Games(name='Chrono Trigger', genres=[genres[0], genres[4]], consoles=[consoles[21], consoles[0], consoles[34]]),
        Games(name='Crash Bandicoot', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Crash Bandicoot 2: Cortex Strikes Back', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Crash Bandicoot: Warped', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Crash Team Racing', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Destruction Derby', genres=[genres[10], genres[15]], consoles=[consoles[0], consoles[24]]),
        Games(name='Digimon Rumble Arena', genres=[genres[0], genres[15]], consoles=[consoles[0]]),
        Games(name='Digimon World', genres=[genres[0], genres[15], genres[4]], consoles=[consoles[0]]),
        Games(name='Digimon World 2', genres=[genres[0], genres[15], genres[4]], consoles=[consoles[0]]),
        Games(name='Digimon World 3', genres=[genres[0], genres[15], genres[4]], consoles=[consoles[0]]),
        Games(name='Dino Crisis', genres=[genres[0]], consoles=[consoles[0], consoles[30]]),
        Games(name='Dragon Ball GT: Final Bout', genres=[genres[15]], consoles=[consoles[0]]),
        Games(name='Final Fantasy VIII', genres=[genres[15], genres[4]], consoles=[consoles[0], consoles[41], consoles[3], consoles[7]]),
        Games(name='Dragon Ball GT: Final Bout', genres=[genres[0], genres[4], genres[12]], consoles=[consoles[0], consoles[28]]),
        Games(name='Medal of Honor', genres=[genres[13], genres[14]], consoles=[consoles[0]]),
        Games(name='Mega Man X6', genres=[genres[0], genres[12], genres[2]], consoles=[consoles[0]]),
        Games(name='Mortal Kombat Trilogy', genres=[genres[15]], consoles=[consoles[0], consoles[24], consoles[27]]),
        Games(name='Pepsiman', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Resident Evil', genres=[genres[0], genres[1], genres[3]], consoles=[consoles[0], consoles[24], consoles[34]]),
        Games(name='Spider Man', genres=[genres[0], genres[15]], consoles=[consoles[0], consoles[27], consoles[30], consoles[28]]),
        Games(name='Spider Man 2: Enter Electro', genres=[genres[0], genres[15]], consoles=[consoles[0]]),
        Games(name='Spyro the Dragon', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Tomb Raider', genres=[genres[0]], consoles=[consoles[0], consoles[24]]),
        Games(name='Tomb Raider II', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name='Tomb Raider III: Adventures of Lara Croft', genres=[genres[0]], consoles=[consoles[0]]),
        Games(name="Tony Hawk's Pro Skater", genres=[genres[11]], consoles=[consoles[0], consoles[27], consoles[28], consoles[30]]),
        Games(name="Tony Hawk's Pro Skater 2", genres=[genres[11]], consoles=[consoles[0], consoles[27], consoles[28], consoles[30], consoles[31]]),
        Games(name='Vigilante 8', genres=[genres[14], genres[10]], consoles=[consoles[0], consoles[27], consoles[28]])
    ]


def create_users(games_query:list):
    users = [
        Users(username = 'admin', email = 'admin@admin.com', password = generate_password_hash('Admin@Py_Trade_Games'), admin = True, since = datetime.datetime.now()),
        Users(username = 'lribeiro', email = 'lucasribeiroalves@live.com', password = generate_password_hash('Flask@2024'), admin = False, games = [g for g in games_query], since = datetime.datetime.now()),
        Users(username = 'seduarte', email = 'selma@hotmail.com', password = generate_password_hash('Flask@2024'), admin = False, games = [games_query[1]], since = datetime.datetime.now()),
    ]