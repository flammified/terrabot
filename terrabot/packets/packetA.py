import struct
import PIL
import zlib
from terrabot.util.streamer import Streamer

class PacketAParser(object):

    def parse(self, world, player, data):
        streamer = Streamer(data)
        streamer.next_byte() #Skip packet number byte
        tiles = []
        compressed = streamer.next_byte()

        if compressed:
            #I dont actually care about compressed packets right now
            #because I dont know how they work yet
            #return
            pass
        print "Compressed: " + str(compressed)

        compressedData = streamer.remainder()
        data = zlib.decompress(compressedData, -zlib.MAX_WBITS);
        streamer =  Streamer(data)

        startx  = streamer.next_int32()
        starty  = streamer.next_int32()
        width   = streamer.next_short()
        height  = streamer.next_short()

        print "StartX: " + str(startx)
        print "StartY: " + str(starty)
        print "Width: " + str(width)
        print "height: " + str(height)


        for i in range(0,height):
            tiles.append([])

        for y in range(0, height):
            for x in range(0, width):
                #Read a tile!
                flag    = streamer.next_byte()
                active  = flag & 2  > 0
                flag2   = flag & 1  > 0
                isShort = flag & 32 > 0
                hasColor    = False
                color = (0, 0, 0)

                if flag2:
                    flag2 = streamer.next_byte()
                    flag3 = flag2 & 1 > 0
                    if flag3:
                        flag3 = streamer.next_byte()
                        hasColor = flag3 & 8 > 0

                if isShort:
                    type = streamer.next_short()
                else:
                    type = streamer.next_byte()

                print type

        print "--------"




#Temporary class, will be moved to own file later on
class Tile(object):
    def __init__(self, x, y, type, color=(0,0,0)):
        self.x = x
        self.y = y
        self.type = type
        self.color = color


