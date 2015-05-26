import packet

class Packet10(packet.Packet):

	def __init__(self,  player):
		super(Packet10, self).__init__(0x10)
		self.addStructuredData("<c", chr(player.playerID))
		self.addStructuredData("<h", player.currHP)
		self.addStructuredData("<h", player.maxHP)

