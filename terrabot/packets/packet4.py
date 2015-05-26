import packet

class Packet4(packet.Packet):

	def __init__(self,  player):
		super(Packet4, self).__init__(4)
		self.addStructuredData("<x", player.playerID)
		self.addStructuredData("<x", player.hairStyle)
		self.addStructuredData("<x", player.gender)

		self.addStructuredData("<x", player.hairColor[0])
		self.addStructuredData("<x", player.hairColor[1])
		self.addStructuredData("<x", player.hairColor[2])

		self.addStructuredData("<x", player.skinColor[0])
		self.addStructuredData("<x", player.skinColor[1])
		self.addStructuredData("<x", player.skinColor[2])

		self.addStructuredData("<x", player.eyeColor[0])
		self.addStructuredData("<x", player.eyeColor[1])
		self.addStructuredData("<x", player.eyeColor[2])

		self.addStructuredData("<x", player.shirtColor[0])
		self.addStructuredData("<x", player.shirtColor[1])
		self.addStructuredData("<x", player.shirtColor[2])

		self.addStructuredData("<x", player.undershirtColor[0])
		self.addStructuredData("<x", player.undershirtColor[1])
		self.addStructuredData("<x", player.undershirtColor[2])

		self.addStructuredData("<x", player.pantsColor[0])
		self.addStructuredData("<x", player.pantsColor[1])
		self.addStructuredData("<x", player.pantsColor[2])

		self.addStructuredData("<x", player.shoeColor[0])
		self.addStructuredData("<x", player.shoeColor[1])
		self.addStructuredData("<x", player.shoeColor[2])

		self.addStructuredData("<x", player.difficulty)

		self.addData(player.name)


