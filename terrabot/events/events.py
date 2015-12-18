import enum

class Events(enum.Enum):
    Chat = 0
    TileUpdate = 1
    Login = 2
    PlayerID = 3
    Blocked = 4
    Initialized = 5
    ItemOwnerChanged = 6
    ItemDropped = 7
    ItemDropUpdate = 8
    NewPlayer = 9
