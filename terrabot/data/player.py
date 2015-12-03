class Player(object):

    def __init__(self, name):
        self.inventory = []
        for i in range(0, 72):
            self.inventory.append("Dummy Item")

        self.playerID = 0
        self.hairStyle = 0x0
        self.gender = 1
        self.hair_color = (255, 255, 255)
        self.skin_color = (255, 255, 255)
        self.eye_color = (255, 255, 255)
        self.shirt_color = (255, 255, 255)
        self.undershirt_color = (255, 255, 255)
        self.pants_color = (255, 255, 255)
        self.shoe_color = (255, 255, 255)
        self.difficulty = 0
        self.name = name

        self.max_hp = 400
        self.currHP = 300

        self.max_mana = 50
        self.curr_mana = 10

        self.initialized = False
        self.logged_in = False
