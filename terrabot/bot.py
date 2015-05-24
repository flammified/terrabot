import socket
import struct
import threading
import packets
import time


class TerraBot(threading.Thread):
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

		self.daemon = True

		self.client = None


	def _initializeConnection(self):
		p1 = packets.Packet1(self.protocol)

	"""Connects to the server and starts the main loop"""
	def startBot(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect(self.ADDR)
		self.running = True
		self.start()
	
	"""Running the bot with using start() will NOT work. Use startBot instead!"""
	def run(self):
		self._initializeConnection()
		while self.running:
			pass


	def stop(self):
		self.running = False		


		

		