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
			if isinstance(t,basestring):
				#Pascal String: length of the string in front of the string
				length += len(t) + len(chr(len(t))) 
			elif isinstance(t, int):
				length += 2
			elif isinstance(t, bool):
				length += 1

		return length

	def addStructuredData(self, newData, structType):
		temp = struct.pack(structType, newData)
		self.addData(temp)

	def addData(self, d):
		#Pascal String: need to add the length
		if isinstance(d, basestring):
			d = chr(len(d)) + d
		self.data.append(d)

	def send(self, client):
		#Adding two, because the length of the packet is also part of the packet
		packet = struct.pack("<h", self._calculateLength()+2)
		packet += chr(self.packetno)
		for i in range(len(self.data)):
			packet += str(self.data[i])
		client.send(packet)

