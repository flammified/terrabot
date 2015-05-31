import struct

class Packet19Parser(object):

	def parse(self, world, player, data):
		print data[6:]