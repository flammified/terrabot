from . import packet

class PacketD(packet.Packet):

	def __init__(self,  player):
		super(PacketC, self).__init__(0xD)
		self.addData(chr(player.playerID))
		self.addData(chr(0))
		self.addData(chr(0))
		self.addStructuredData("<f", world.spawnX)
		self.addStructuredData("<f", world.spawnY)
		self.addStructuredData("<f", 0)
		self.addStructuredData("<f", 0)
		self.addData(chr(255))
