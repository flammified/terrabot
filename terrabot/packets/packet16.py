from terrabot.util.streamer import Streamer
from terrabot.events import Events

class Packet16Parser(object):

	def parse(self, world, player, data, ev_man):
		streamer = Streamer(data)
		streamer.next_byte() # Ignore packet number
		item_id = streamer.next_short()
		owner_id = streamer.next_byte()

		ev_man.raise_event(Events.ItemOwnerChanged, (owner_id, item_id))
