import packet

class Packet32(packet.Packet):

	def __init__(self,  player):
		super(Packet10, self).__init__(0x32)
		self.addStructuredData("<x", player.playerID)
		for i in range(0, 10):
			self.addStructuredData("<x", 0)

