from terrabot.util.streamer import Streamer
from terrabot.events.events import Events
from terrabot.data.item import Item

class Packet15Parser(object):

	def parse(self, world, player, data, ev_man):
		streamer = Streamer(data)
		streamer.next_byte() #Skip packet byte
		item_id = streamer.next_short()
		position = (streamer.next_float(), streamer.next_float())
		velocity = (streamer.next_float(), streamer.next_float())
		stacks = streamer.next_short()
		prefix = streamer.next_byte()
		no_delay = streamer.next_byte()
		net_id = streamer.next_short()

		if item_id < 400 and net_id == 0:
			return
		if item_id is 400:
			world.items.append(item)

		item_object = Item(item_id, net_id, position, velocity, prefix, stacks)

		ev_man.raise_event(Events.ItemDropUpdate, item_object)
