import zlib

from terrabot.data.tile import Tile
from terrabot.util.tileutil import *
from terrabot.util.streamer import Streamer

from terrabot.events.events import Events


class PacketAParser(object):
    def parse(self, world, player, data, ev_man):
        streamer = Streamer(data)
        streamer.next_byte()  # Skip packet number byte
        compressed = streamer.next_byte()

        # print("Compressed: " + str(compressed))

        if compressed:
            compressed_data = streamer.remainder()
            data = zlib.decompress(compressed_data, -zlib.MAX_WBITS)
            streamer = Streamer(data)

        startx = streamer.next_int32()
        starty = streamer.next_int32()
        width = streamer.next_short()
        height = streamer.next_short()

        # print("StartX: " + str(startx))
        # print("StartY: " + str(starty))
        # print("Width: " + str(width))
        # print("Height: " + str(height))
        # #print "ByteLength: " + str(len(streamer.remainder()))

        repeat_count = 0
        last_tile = None

        for y in range(height):
            for x in range(width):
                if repeat_count > 0:
                    repeat_count -= 1
                    world.tiles[starty + y][startx + x] = last_tile
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

                    #print str(int(active)) + " " + str(int(has_wall)) + " " + str(int(liquid)) + " " + str(int(is_short)) + " " + str(int(repeat_value_present)) + " " + str(int(extra_repeat_value))

                    # if not repeat_value_present and extra_repeat_value:
                    #     print("WTF")

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
                    temp_tile = Tile(tile_type=tile_type, active=active, color=color)
                    last_tile = temp_tile
                    world.tiles[starty + y][startx + x] = temp_tile

        ev_man.raise_event(Events.TileUpdate, world.tiles)
