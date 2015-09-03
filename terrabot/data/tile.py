# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, tile_type=0, active=True, color=(0, 0, 0)):
        self.active = active
        self.type = tile_type
        self.color = color
