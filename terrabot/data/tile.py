

# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, active=True, tile_type=0, color=(0, 0, 0)):
        self.active = active
        self.type = tile_type
        self.color = color
