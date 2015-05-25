class Player(object):

	def __init__(self):
		self.inventory = []
		for i in range(0,72):
			self.inventory.append("Dummy Item")

		self.hairStyle = 0
		self.hairColor = 0

		self.playerID = 0

		#etc