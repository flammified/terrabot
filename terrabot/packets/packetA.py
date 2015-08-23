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
        print "Height: " + str(height)
        print "ByteLength: " + str(len(streamer.remainder()))

        for i in range(0, height):
            tiles.append([])

        repeat_count = 0
        last_tile = None

        for y in range(0, height):
            for x in range(0, width):
                if repeat_count > 0:
                    repeat_count -= 1
                    tiles[y].append(last_tile)
                    x += 1
                    if x > width:
                        y += 1
                    continue

                flag = streamer.next_byte()
                flag2 = streamer.next_byte()
                flag3 = streamer.next_byte()

                active = flag & 2 > 0
                is_short = flag & 32 > 1
                liquid = flag & 8 > 1
                has_wall = flag & 4 > 1
                repeat_value_present = flag & 64 > 1
                extra_repeat_value = (flag & 128) > 0

                wire = flag2 & 2 == 1
                wire2 = flag2 & 4 == 1
                wire3 = flag2 & 8 == 1

                has_color = flag3 & 8 == 1
                has_wall_color = flag3 & 16 == 1

                frame_y = 0
                frame_x = 0
                wall = 0
                wall_color = 0
                tile_type = 0
                frame_important = False
                color = (0, 0, 0)
                has_color = False
                has_wall_color = False

                if active:
                    if is_short:
                        t = streamer.next_short()
                    else:
                        t = streamer.next_byte()
                    if frame_important:
                        frame_x = streamer.read_short()
                        frame_y = streamer.read_short()
                    if has_color:
                        color = streamer.next_byte()
                if has_wall:
                    wall = streamer.next_byte()
                if has_wall and has_wall_color:
                    wall_color = streamer.next_byte()
                if liquid:
                    streamer.next_byte()
                if wire:
                    streamer.next_byte()
                if wire2:
                    streamer.next_byte()
                if wire3:
                    streamer.next_byte()
                if repeat_value_present:
                    if extra_repeat_value:
                        repeat_count = streamer.next_short()
                    else:
                        repeat_count = streamer.next_byte()
                temp_tile = Tile(x, y)
                last_tile = temp_tile
                tiles[y].append(temp_tile)
                #print str(len(streamer.remainder()))
                #print "XY: " + str(x) + " : " + str(y) + " Rem: " + str(len(streamer.remainder()))

        #print "Width: " + str(len(tiles[0]))
        #print "Height: " + str(len(tiles))

        print "--------"


# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, x, y, active=True, tile_type=0, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.active = active
        self.type = tile_type
        self.color = color
