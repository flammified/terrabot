import struct
from terrabot.util.streamer import Streamer

#For temporary drawing of sections
import PIL

class PacketAParser(object):

	def parse(self, world, player, data):

		print "Section Data"

		streamer = Streamer(data)
		streamer.nextByte() #Skip packet number byte
		tiles = []
		compressed = streamer.nextByte()
		if compressed:
			#I dont actually care about compressed packets right now
			#because I dont know how they work yet
			return

		startx 	= streamer.nextInt32()
		starty 	= streamer.nextInt32()
		width 	= streamer.nextShort()
		height 	= streamer.nextShort()

		print "StartX: " + str(startx)
		print "StartY: " + str(starty)
		print "Width: " + str(width)
		print "height: " + str(height)


		for i in range(0,height):
			tiles.append([])

		for y in range(0, height):
			for x in range(0, width):
				#Read a tile!
				flag 	= streamer.nextByte()
				active 	= flag & 2 	> 0
				flag2 	= flag & 1 	> 0
				isShort	= flag & 32 > 0
				hasColor 	= False
				color = (0, 0, 0)

				if flag2:
					flag2 = streamer.nextByte()
					flag3 = flag2 & 1 > 0
					if flag3:
						flag3 = streamer.nextByte()
						hasColor = flag3 & 8 > 0

				if isShort:
					type = streamer.nextShort()
				else:
					type = streamer.nextByte()

				print type




#Temporary class, will be moved to own file later on
class Tile(object):
	def __init__(self, x, y, type, color=(0,0,0)):
		self.x = x
		self.y = y
		self.type = type
		self.color = color


