from terrabot.util.streamer import Streamer

class Packet16Parser(object):

	def parse(self, world, player, data, ev_man):
		streamer = Streamer(data)
		streamer.next_byte() # Ignore packet number
		item_id = streamer.next_short()
		owner_id = streamer.next_byte()
