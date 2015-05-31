import packet

class Packet4(packet.Packet):

	def __init__(self,  player):
		super(Packet4, self).__init__(4)
		self.addData(chr(player.playerID))
		self.addData(chr(player.gender))
		self.addData(chr(player.hairStyle))
		self.addData(player.name, pascalString=True)
		self.addData(chr(0)) #HairStyle
		self.addData(chr(1)) #HideVisual?

		self.addData(chr(player.hairColor[0]))
		self.addData(chr(player.hairColor[1]))
		self.addData(chr(player.hairColor[2]))

		self.addData(chr(player.skinColor[0]))
		self.addData(chr(player.skinColor[1]))
		self.addData(chr(player.skinColor[2]))

		self.addData(chr(player.eyeColor[0]))
		self.addData(chr(player.eyeColor[1]))
		self.addData(chr(player.eyeColor[2]))

		self.addData(chr(player.shirtColor[0]))
		self.addData(chr(player.shirtColor[1]))
		self.addData(chr(player.shirtColor[2]))

		self.addData(chr(player.undershirtColor[0]))
		self.addData(chr(player.undershirtColor[1]))
		self.addData(chr(player.undershirtColor[2]))

		self.addData(chr(player.pantsColor[0]))
		self.addData(chr(player.pantsColor[1]))
		self.addData(chr(player.pantsColor[2]))

		self.addData(chr(player.shoeColor[0]))
		self.addData(chr(player.shoeColor[1]))
		self.addData(chr(player.shoeColor[2]))

		self.addData(chr(player.difficulty))



