from terrabot.util.streamer import Streamer
from terrabot.events import Events
from . import packet

class Packet16(packet.Packet):

	def __init__(self, item_id, owner_id):
		super(Packet16, self).__init__(22)
		self.add_structured_data('<h', item_id)
		self.add_data(owner_id)

class Packet16Parser(object):

	def parse(self, world, player, data, ev_man):
		streamer = Streamer(data)
		streamer.next_byte() # Ignore packet number
		item_id = streamer.next_short()
		owner_id = streamer.next_byte()

		ev_man.raise_event(Events.ItemOwnerChanged, (owner_id, item_id))
