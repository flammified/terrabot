from . import packet


class Packet32(packet.Packet):

    def __init__(self, player):
        super(Packet32, self).__init__(0x32)
        self.add_data(player.playerID)
        for i in range(0, 22):
            self.add_data(0)
