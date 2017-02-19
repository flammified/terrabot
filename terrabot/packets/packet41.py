from . import packet


class Packet41(packet.Packet):

    def __init__(self, id, x, y):
        super(Packet41, self).__init__(0x41)
        self.add_data(2)  # Player tp flag
        self.add_data(id)
        self.add_structured_data("<h", x)
        self.add_structured_data("<h", y)
