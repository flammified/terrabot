import PIL
import zlib
from terrabot.util.streamer import Streamer

class PacketAParser(object):

    def parse(self, world, player, data):
        streamer = Streamer(data)
        streamer.next_byte() #Skip packet number byte
        tiles = []
        compressed = streamer.next_byte()

        print "Compressed: " + str(compressed)

        compressed_data = streamer.remainder()
        data = zlib.decompress(compressed_data, -zlib.MAX_WBITS)
        streamer = Streamer(data)

        startx = streamer.next_int32()
        starty = streamer.next_int32()
        width = streamer.next_short()
        height = streamer.next_short()

        print "StartX: " + str(startx)
        print "StartY: " + str(starty)
        print "Width: " + str(width)
        print "height: " + str(height)

        for i in range(0,height):
            tiles.append([])

        repeat_count = 0
        last_tile = None
        for y in range(0, height):
            for x in range(0, width):
                if repeat_count > 0:
                    repeat_count -= 1
                    tiles[x][y] = last_tile
                    continue
                flag = streamer.next_byte()
                active = flag & 2 > 0
                flag2 = flag & 1 > 0
                is_short = flag & 32 > 0
                has_color = False
                color = (0, 0, 0)

                if flag2:
                    flag2 = streamer.next_byte()
                    flag3 = flag2 & 1 > 0
                    if flag3:
                        flag3 = streamer.next_byte()
                        has_color = flag3 & 8 > 0

                if is_short:
                    t = streamer.next_short()
                else:
                    t = streamer.next_byte()

                last_tile = tiles[x][y]

        print "--------"


# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, x, y, t, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.type = t
        self.color = color
