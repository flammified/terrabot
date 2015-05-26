import packet

class Packet4(packet.Packet):

	def __init__(self,  player):
		super(Packet4, self).__init__(4)
		self.addStructuredData("<c", chr(player.playerID))
		self.addStructuredData("<c", chr(player.hairStyle))
		self.addStructuredData("<c", chr(player.gender))

		self.addStructuredData("<c", chr(player.hairColor[0]))
		self.addStructuredData("<c", chr(player.hairColor[1]))
		self.addStructuredData("<c", chr(player.hairColor[2]))

		self.addStructuredData("<c", chr(player.skinColor[0]))
		self.addStructuredData("<c", chr(player.skinColor[1]))
		self.addStructuredData("<c", chr(player.skinColor[2]))

		self.addStructuredData("<c", chr(player.eyeColor[0]))
		self.addStructuredData("<c", chr(player.eyeColor[1]))
		self.addStructuredData("<c", chr(player.eyeColor[2]))

		self.addStructuredData("<c", chr(player.shirtColor[0]))
		self.addStructuredData("<c", chr(player.shirtColor[1]))
		self.addStructuredData("<c", chr(player.shirtColor[2]))

		self.addStructuredData("<c", chr(player.undershirtColor[0]))
		self.addStructuredData("<c", chr(player.undershirtColor[1]))
		self.addStructuredData("<c", chr(player.undershirtColor[2]))

		self.addStructuredData("<c", chr(player.pantsColor[0]))
		self.addStructuredData("<c", chr(player.pantsColor[1]))
		self.addStructuredData("<c", chr(player.pantsColor[2]))

		self.addStructuredData("<c", chr(player.shoeColor[0]))
		self.addStructuredData("<c", chr(player.shoeColor[1]))
		self.addStructuredData("<c", chr(player.shoeColor[2]))

		self.addStructuredData("<c", chr(player.difficulty))

		self.addData(player.name)


