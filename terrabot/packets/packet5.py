import packet

class Packet5(packet.Packet):

	def __init__(self,  player, slot):
		super(Packet5, self).__init__(0x5)
		self.addStructuredData("<c", chr(player.playerID))
		self.addStructuredData("<c", chr(slot))
		self.addStructuredData("<h", 0) #Stack
		self.addStructuredData("<c", chr(0)) #Prefix
		self.addStructuredData("<h", 0) #ItemID
