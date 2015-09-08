from . import packet


class Packet19Parser(object):

    def parse(self, world, player, data):
        if data[1] != player.playerID:
            print(data[6:])


class Packet19(packet.Packet):

    def __init__(self, player, msg=":)"):
        super(Packet19, self).__init__(0x19)
        self.add_data(player.playerID)
        self.add_data(1)
        self.add_data(1)
        self.add_data(1)
        self.add_data(msg, pascal_string=True)
