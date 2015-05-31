import struct

class Packet(object):

	#Data is an array containing the payload of the packet: the length does not need to be set but is calculated dynamically
	def __init__(self, packetno):
		self.packetno = packetno
		self.data = []

	def _calculateLength(self):
		length = 0;
		for i in range(len(self.data)):
			t = self.data[i]
			length += t[1]

		return length

	def addStructuredData(self, structType, newData):
		temp = struct.pack(structType, newData)
		self.data.append((temp, struct.calcsize(structType)))

	def addData(self, d, pascalString=False):
		#Pascal String: need to add the length

		length = len(d)
		if pascalString:
			print d
			d = chr(length) + d
			length = len(d)
		self.data.append((d, length))

	def send(self, client):
		#Adding two, because the length of the packet is also part of the packet
		packet = struct.pack("<h", self._calculateLength()+3)
		packet += chr(self.packetno)
		for i in range(len(self.data)):
			packet += str(self.data[i][0])
		client.send(packet)

