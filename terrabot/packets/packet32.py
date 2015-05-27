import packet

class Packet32(packet.Packet):

	def __init__(self,  player):
		super(Packet32, self).__init__(0x32)
		self.addStructuredData("<c", chr(player.playerID))
		for i in range(0, 10):
			self.addStructuredData("<c", chr(0))

