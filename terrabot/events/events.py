import enum


class Events(enum.Enum):
    # Trigger: chat message
    # Data: message as string
    Chat = 0

    # Trigger: Tile information
    # Data: 2D array of Tiles
    TileUpdate = 1

    # Trigger: Login
    # Data: null
    Login = 2

    # Trigger: PlayerID packet comes in
    # Data: PlayerID as int
    PlayerID = 3

    # Trigger: Access blocked
    # Data: reason-message as string
    Blocked = 4

    # Trigger: Initialization on the server
    # Data: null
    Initialized = 5

    # Trigger: Item owner changes
    # Data: Tuple: (item_id, owner_id)
    ItemOwnerChanged = 6

    # Trigger: A new item drops
    # Data: Item object
    ItemDropped = 7

    # Trigger: Server sends update on an item
    # Data: Item object
    ItemDropUpdate = 8

    # Trigger: A new player joins
    # Data: PlayerID
    NewPlayer = 9
