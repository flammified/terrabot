import packet


class Packet4(packet.Packet):

    def __init__(self, player):
        super(Packet4, self).__init__(4)
        self.add_data(chr(player.playerID))
        self.add_data(chr(4))  # player.gender))
        self.add_data(chr(player.hairStyle))
        self.add_data(player.name, pascal_string=True)
        self.add_data(chr(0))  # HairStyle
        self.add_data(chr(1))  # HideVisual?

        self.add_data(chr(player.hairColor[0]))
        self.add_data(chr(player.hairColor[1]))
        self.add_data(chr(player.hairColor[2]))

        self.add_data(chr(player.skinColor[0]))
        self.add_data(chr(player.skinColor[1]))
        self.add_data(chr(player.skinColor[2]))

        self.add_data(chr(player.eyeColor[0]))
        self.add_data(chr(player.eyeColor[1]))
        self.add_data(chr(player.eyeColor[2]))

        self.add_data(chr(player.shirtColor[0]))
        self.add_data(chr(player.shirtColor[1]))
        self.add_data(chr(player.shirtColor[2]))

        self.add_data(chr(player.undershirtColor[0]))
        self.add_data(chr(player.undershirtColor[1]))
        self.add_data(chr(player.undershirtColor[2]))

        self.add_data(chr(player.pantsColor[0]))
        self.add_data(chr(player.pantsColor[1]))
        self.add_data(chr(player.pantsColor[2]))

        self.add_data(chr(player.shoeColor[0]))
        self.add_data(chr(player.shoeColor[1]))
        self.add_data(chr(player.shoeColor[2]))

        self.add_data(chr(player.difficulty))
