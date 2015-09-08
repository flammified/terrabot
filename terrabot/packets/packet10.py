from . import packet


class Packet10(packet.Packet):

    def __init__(self, player):
        super(Packet10, self).__init__(0x10)
        self.add_data(player.playerID)
        self.add_structured_data("<h", player.currHP)
        self.add_structured_data("<h", player.maxHP)
