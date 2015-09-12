import struct


class Packet(object):

    # Data is an array containing the payload of the packet:
    # the length does not need to be set but is calculated dynamically
    def __init__(self, packetno):
        self.packetno = packetno
        self.data = bytearray()

    def _calculate_length(self):
        return len(self.data)

    def add_structured_data(self, struct_type, new_data):
        temp = struct.pack(struct_type, new_data)
        self.data.extend(temp)

    def add_data(self, d, pascal_string=False):
        # Pascal String: need to add the length using a signed
        # char
        if pascal_string:
            length = len(d)
            d = bytes(d, 'utf-8')
            self.data += struct.pack('<b', length)
            self.data += d
        else:
            self.data += bytes([d])

    def send(self, client):
        # Adding 3, because the length of the packet (short) and packno
        # (a byte) are also part of the packet
        packet = struct.pack("<h", self._calculate_length() + 3)
        packet += struct.pack('b', self.packetno)
        packet += self.data
        client.send(packet)
