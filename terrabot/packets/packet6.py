from . import packet

class Packet6(packet.Packet):

	def __init__(self):
		super(Packet6, self).__init__(0x6)
		
