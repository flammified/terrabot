class Player(object):

    def __init__(self, name):
        self.inventory = []
        for i in range(0, 72):
            self.inventory.append("Dummy Item")

        self.playerID = 0
        self.hairStyle = 0x0
        self.gender = 1
        self.hairColor = (255, 255, 255)
        self.skinColor = (255, 255, 255)
        self.eyeColor = (255, 255, 255)
        self.shirtColor = (255, 255, 255)
        self.undershirtColor = (255, 255, 255)
        self.pantsColor = (255, 255, 255)
        self.shoeColor = (255, 255, 255)
        self.difficulty = 0
        self.name = name


        self.maxHP = 400
        self.currHP = 300

        self.maxMana = 50
        self.currMana = 10

        self.initialized = False
        self.logged_in = False
