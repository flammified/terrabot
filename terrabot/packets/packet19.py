from . import packet
from terrabot.util.streamer import Streamer

class Packet19Parser(object):

    def parse(self, world, player, data):
        streamer = Streamer(data)
        streamer.next_byte() # Skip packet id
        id = streamer.next_byte()
        if id != player.playerID:
            color = (streamer.next_byte(),
                    streamer.next_byte(),
                    streamer.next_byte())
            length = streamer.next_byte()
            print(streamer.remainder())

class Packet19(packet.Packet):

    def __init__(self, player, msg=":)"):
        super(Packet19, self).__init__(0x19)
        self.add_data(player.playerID)
        self.add_data(1)
        self.add_data(1)
        self.add_data(1)
        self.add_data(msg, pascal_string=True)
