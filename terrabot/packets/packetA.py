import PIL
import zlib
from terrabot.util.tileutil import *
from terrabot.util.streamer import Streamer


class PacketAParser(object):
    def parse(self, world, player, data):
        streamer = Streamer(data)
        streamer.next_byte()  # Skip packet number byte
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
        #print "ByteLength: " + str(len(streamer.remainder()))

        for i in range(height):
            tiles.append([])

        repeat_count = 0
        last_tile = None

        for y in range(height):
            for x in range(width):
                if repeat_count > 0:
                    repeat_count -= 1
                    tiles[y].append(last_tile)
                else:
                    flag = streamer.next_byte()
                    flag2 = 0
                    flag3 = 0
                    if flag & 1:
                        flag2 = streamer.next_byte()
                    if flag2 & 1:
                        flag3 = streamer.next_byte()

                    active = flag & 2 > 0
                    has_wall = flag & 4 > 0
                    liquid = flag & 8 > 0
                    is_short = flag & 32 > 0
                    repeat_value_present = flag & 64 > 0
                    extra_repeat_value = flag & 128 > 0

                    print str(int(active)) + " " + str(int(has_wall)) + " " + str(int(liquid)) + " " + str(int(is_short)) + " " + str(int(repeat_value_present)) + " " + str(int(extra_repeat_value))

                    if not repeat_value_present and extra_repeat_value:
                        print "WTF"

                    wire = flag2 & 2 > 0
                    wire2 = flag2 & 4 > 0
                    wire3 = flag2 & 8 > 0

                    has_color = flag3 & 8 > 0
                    has_wall_color = flag3 & 16 > 0

                    frame_y = 0
                    frame_x = 0
                    wall = 0
                    wall_color = 0
                    tile_type = 0
                    color = (0, 0, 0)

                    if active:
                        if is_short:
                            tile_type = streamer.next_short()
                        else:
                            tile_type = streamer.next_byte()
                        if tile_type in frameImportant:
                            frame_x = streamer.next_short()
                            frame_y = streamer.next_short()
                    if has_color:
                        color = streamer.next_byte()
                    if has_wall:
                        wall = streamer.next_byte()
                        if has_wall_color:
                            wall_color = streamer.next_byte()
                    if liquid:
                        streamer.next_byte()
                    if wire:
                        streamer.next_byte()
                    if wire2:
                        streamer.next_byte()
                    if wire3:
                        streamer.next_byte()
                    if extra_repeat_value:
                        repeat_count = streamer.next_short()
                    else:
                        if repeat_value_present:
                            repeat_count = streamer.next_byte()
                    # print str(frame_x) + " " + str(frame_y) + " " + str(wall) + " " + str(wall_color) + " " + str(tile_type) + " " + str(color) + " " + str(repeat_count)
                    temp_tile = Tile()
                    last_tile = temp_tile
                    tiles[y].append(temp_tile)
            # print str(len(streamer.remainder()))
            # print "XY: " + str(x) + " : " + str(y) + " Rem: " + str(len(streamer.remainder()))
        # print "Width: " + str(len(tiles[0]))
        # print "Height: " + str(len(tiles))
        print "-------------------------"


# Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, active=True, tile_type=0, color=(0, 0, 0)):
        self.active = active
        self.type = tile_type
        self.color = color
