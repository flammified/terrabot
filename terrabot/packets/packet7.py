import struct
from terrabot.util.streamer import Streamer

class Packet7Parser(object):

	def parse(self, world, player, data, ev_man):
		streamer = Streamer(data)
		streamer.next_byte() # Ignore packet ID byte
		world.time = streamer.next_int32()
		world.daynight = streamer.next_byte()
		world.moonphase = streamer.next_byte()
		world.maxX = streamer.next_short()
		world.maxY = streamer.next_short()
		world.spawnX = streamer.next_short()
		world.spawnY = streamer.next_short()
		world.initialize_tiles(world.maxX, world.maxY)
