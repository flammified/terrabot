from . import packet


class Packet4(packet.Packet):

    def __init__(self, player):
        super(Packet4, self).__init__(4)
        self.add_data(player.playerID)
        self.add_data(4)  # Skin
        self.add_data(player.hairStyle)
        self.add_data(player.name, pascal_string=True)
        self.add_data(0)  # HairStyle
        self.add_data(1)  # HideVisual?
        self.add_data(1)  # HideVisual2?
        self.add_data(0)  # Hide miscs

        self.add_data(player.hairColor[0])
        self.add_data(player.hairColor[1])
        self.add_data(player.hairColor[2])

        self.add_data(player.skinColor[0])
        self.add_data(player.skinColor[1])
        self.add_data(player.skinColor[2])

        self.add_data(player.eyeColor[0])
        self.add_data(player.eyeColor[1])
        self.add_data(player.eyeColor[2])

        self.add_data(player.shirtColor[0])
        self.add_data(player.shirtColor[1])
        self.add_data(player.shirtColor[2])

        self.add_data(player.undershirtColor[0])
        self.add_data(player.undershirtColor[1])
        self.add_data(player.undershirtColor[2])

        self.add_data(player.pantsColor[0])
        self.add_data(player.pantsColor[1])
        self.add_data(player.pantsColor[2])

        self.add_data(player.shoeColor[0])
        self.add_data(player.shoeColor[1])
        self.add_data(player.shoeColor[2])

        self.add_data(player.difficulty)
