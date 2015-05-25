import socket
import struct
import threading
import packets

class TerraBot(object):
	"""A bot for a terraria server"""

	#Defaults to 7777, because that is the default port for the server
	def __init__(self, ip, port=7777, protocol=102, name="Terrabot"):
		super(TerraBot, self).__init__()

		self.HOST = ip
		self.PORT = port
		self.ADDR  = (self.HOST, self.PORT)

		self.protocol = protocol
		self.name = name
		self.running = False

		self.writeThread = threading.Thread(target = self.readPackets)
		self.writeThread.daemon = True

		self.readThread = threading.Thread(target = self.sendPackets)
		self.readThread.daemon = True

		self.client = None

		self.writeQueue = []

		#Information about the player


	def _initializeConnection(self):
		p1 = packets.Packet1(self.protocol)

	"""Connects to the server and starts the main loop"""
	def start(self):
		if not self.writeThread.isAlive() and not self.readThread.isAlive():
			self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.client.connect(self.ADDR)
			self.running = True	
			self.writeThread.start()
			self.readThread.start()
			self.writeQueue.append(packets.Packet1(self.protocol))

	def readPackets(self):
		while self.running:
			packet_length = self.client.recv(2)
			packet_length = struct.unpack("<h", packet_length)[0]-2
			print packet_length
			data = self.client.recv(packet_length)

			command = ord(data[0])

	def sendPackets(self):
		while self.running:
			if len(self.writeQueue) > 0:
				self.writeQueue[0].send(self.client)
				self.writeQueue.pop(0)

	def stop(self):
		self.running = False		


		

		