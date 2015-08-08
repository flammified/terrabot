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

        if compressed:
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
                    tiles[y].add(last_tile)
                    continue
                flag = streamer.next_byte()
                active = flag & 2 == 1
                flag2_exists = flag & 1 == 1
                is_short = flag & 32 == 1
                has_wall = flag & 4 == 1
                repeat_value_present = flag & 64 == 1
                extra_repeat_value = flag & 128 == 1

                frame_y = 0
                frame_y = 0
                wall = 0
                wall_color = 0
                tile_type = 0
                frame_important = False
                color = (0, 0, 0)
                has_color = False
                has_wall_color = False

                if active:
                    if flag2_exists:
                        flag2 = streamer.next_byte()
                        flag3 = flag2 & 1 == 1
                        if flag3:
                            flag3 = streamer.next_byte()
                            has_color = flag3 & 8 == 1
                            has_wall_color = flag3 & 16 == 1
                    if is_short:
                        t = streamer.next_short()
                    else:
                        t = streamer.next_byte()
                    if frame_important:
                        frame_x = streamer.read_short()
                        frame_y = streamer.read_short()
                if has_color:
                    color = (streamer.next_short(), streamer.next_short(), streamer.next_short())
                if has_wall:
                    wall = streamer.next_byte()
                if has_wall and has_wall_color:
                    wall_color = (streamer.next_short(), streamer.next_short(), streamer.next_short())

                temp_tile = Tile()
                last_tile = temp_tile
                tiles[y].add(temp_tile)

        print "--------"


# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, x, y, active=True, tile_type=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.active = active
        self.type = tile_type
        self.color = color
