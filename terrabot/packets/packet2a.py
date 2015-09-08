from . import packet


class Packet2A(packet.Packet):

    def __init__(self, player):
        super(Packet2A, self).__init__(0x2A)
        self.add_data(player.playerID)
        self.add_structured_data("<h", player.currMana)
        self.add_structured_data("<h", player.maxMana)
