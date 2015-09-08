from .tile import Tile

class World:

    def __init__(self):
        self.moon = 0
        self.spawnX = 0
        self.spawnY = 0
        self.time = 0

    def initialize_tiles(self, width, height):
        self.tiles =  [[None for x in range(0, width)]
        for y in range(0, height)]
