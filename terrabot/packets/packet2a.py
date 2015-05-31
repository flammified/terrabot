import packet

class Packet2A(packet.Packet):

	def __init__(self,  player):
		super(Packet2A, self).__init__(0x2A)
		self.addData(chr(player.playerID))
		self.addStructuredData("<h", player.currMana)
		self.addStructuredData("<h", player.maxMana)

