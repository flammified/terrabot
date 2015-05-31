import packet

class Packet8(packet.Packet):

	def __init__(self,  player, world):
		super(Packet8, self).__init__(0x8)
		self.addStructuredData("<i", world.spawnX)
		self.addStructuredData("<i", world.spawnY)

