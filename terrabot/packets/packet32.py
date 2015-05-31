import packet

class Packet32(packet.Packet):

	def __init__(self,  player):
		super(Packet32, self).__init__(0x32)
		self.addData(chr(player.playerID))
		for i in range(0, 22):
			self.addData(chr(0))

