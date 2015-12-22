from terrabot.util.streamer import Streamer

class Packet39Parser(object):

    def parse(self, world, player, data, ev_man):
        streamer = Streamer(data)
        streamer.next_byte() #Skip packet number
        item_index = streamer.next_short()

        world.item_owner_index[item_index] = 255
