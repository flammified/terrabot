import struct

class Streamer(object):
	"""A class for streaming numbers from a databuffer."""

	def __init__(self, data):
		self.data = data
		self.index = 0

	def nextShort(self):
		print "Index: " + str(self.index) + " datalength " + str(len(self.data))
		result = struct.unpack("<h", self.data[self.index : self.index + 2])[0]
		self.index += 2
		return result

	def nextInt32(self):
		result = struct.unpack("<i", self.data[self.index : self.index + 4])[0]
		self.index += 4
		return result

	def nextByte(self):
		result = ord(self.data[self.index])
		self.index += 1
		return result

