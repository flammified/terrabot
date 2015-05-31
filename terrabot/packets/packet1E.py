import packet

class Packet1E(packet.Packet):

	def __init__(self,  player):
		super(Packet1E, self).__init__(0x1E)
		self.addData(chr(player.playerID))
		self.addData(chr(1))

