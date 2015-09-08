from . import packet


#Does not work?
class Packet3D(packet.Packet):

	def __init__(self,  player):
		super(Packet3D, self).__init__(0x3D)
		self.addData(chr(player.playerID))
		self.addData(chr(1))

