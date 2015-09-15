import enum

class Events(enum.Enum):
    Chat = 0
    TileUpdate = 1
    Spawn = 2
    PlayerID = 3
    Blocked = 4

print(type(Events))
