from . import packet


class Packet1E(packet.Packet):

    def __init__(self, player):
        super(Packet1E, self).__init__(0x1E)
        self.add_data(chr(player.playerID))
        self.add_data(chr(1))
