import struct


class Packet(object):

    # Data is an array containing the payload of the packet:
    # the length does not need to be set but is calculated dynamically
    def __init__(self, packetno):
        self.packetno = packetno
        self.data = []

    def _calculate_length(self):
        length = 0
        for i in range(len(self.data)):
            t = self.data[i]
            length += t[1]

        return length

    def add_structured_data(self, struct_type, new_data):
        temp = struct.pack(struct_type, new_data)
        self.data.append((temp, struct.calcsize(struct_type)))

    def add_data(self, d, pascal_string=False):
        # Pascal String: need to add the length

        length = len(d)
        if pascal_string:
            d = chr(length) + d
            length = len(d)
        self.data.append((d, length))

    def send(self, client):
        # Adding 3, because the length of the packet and packno
        # are also part of the packet
        packet = struct.pack("<h", self._calculate_length() + 3)
        packet += chr(self.packetno)
        print self.data
        for i in range(len(self.data)):
            packet += str(self.data[i][0])
        client.send(packet)
