import packet

class Packet5(packet.Packet):

	def __init__(self,  player, slot):
		super(Packet5, self).__init__(0x5)
		self.addData(chr(player.playerID))
		self.addData(chr(slot))
		self.addStructuredData("<h", 0) #Stack
		self.addData(chr(0)) #Prefix
		self.addStructuredData("<h", 0) #ItemID
