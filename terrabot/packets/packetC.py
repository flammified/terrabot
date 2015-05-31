import packet

class PacketC(packet.Packet):

	def __init__(self,  world):
		super(PacketC, self).__init__(0xC)
		self.addData(chr(player.playerID))
		self.addStructuredData("<i", world.spawnX)
		self.addStructuredData("<i", world.spawnY)

