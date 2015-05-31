import packet

class PacketD(packet.Packet):

	def __init__(self,  player):
		super(PacketC, self).__init__(0xD)
		self.addData(chr(player.playerID))
		self.addData(chr(D))
