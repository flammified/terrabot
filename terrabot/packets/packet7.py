import struct
from terrabot.util.streamer import Streamer

class Packet7Parser(object):

	def parse(self, world, player, data):
		streamer = Streamer(data)
		streamer.next_byte() # Ignore packet ID byte
		world.time = streamer.next_int32()
		world.daynight = streamer.next_byte()
		world.moonphase = streamer.next_byte()
		world.maxX = streamer.next_short()
		world.maxY = streamer.next_short()
		world.spawnX = streamer.next_short()
		world.spawnY = streamer.next_short()
		world.tiles = [[0 for x in range(0, world.maxX) for y in range(0, world.maxY)]]
		print str(world.maxX) + " " + str(world.maxY)
