import packet


class PacketC(packet.Packet):

    def __init__(self, player, world):
        super(PacketC, self).__init__(0xC)
        self.addData(chr(player.playerID))
        self.addStructuredData("<h", world.spawnX)
        self.addStructuredData("<h", world.spawnY)
