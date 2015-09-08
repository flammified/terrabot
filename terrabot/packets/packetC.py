from . import packet


class PacketC(packet.Packet):

    def __init__(self, player, world):
        super(PacketC, self).__init__(0xC)
        self.add_data(player.playerID)
        self.add_structured_data("<h", world.spawnX)
        self.add_structured_data("<h", world.spawnY)
