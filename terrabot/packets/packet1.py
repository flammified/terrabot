from . import packet


class Packet1(packet.Packet):

    def __init__(self, protocol):
        super(Packet1, self).__init__(1)
        self.add_data("Terraria" + str(protocol), pascal_string=True)
