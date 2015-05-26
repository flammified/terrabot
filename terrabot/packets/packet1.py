import packet

class Packet1(packet.Packet):

	def __init__(self,  protocol):
		super(Packet1, self).__init__(1)
		self.addData("Terraria" + str(protocol))
