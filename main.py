from terrabot import TerraBot
import threading, time

#For running from main, will be removed later
from terrabot.packets.packet1 import Packet1
import socket
import struct
import sys

if (__name__ == "__main__"):

	RUN_FROM_MAIN = False

	HOST = '127.0.0.1'
	PORT = 7777
	PLAYERNAME = 'Terrabot'

	if (len(sys.argv) > 1):
		HOST = sys.argv[1]
	if (len(sys.argv) > 2):
		PLAYERNAME = sys.argv[2]
	ADDR = (HOST, PORT)
	protocol = 102

	if RUN_FROM_MAIN:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect(ADDR)

		"""
		data = chr(len(str(protocol)) + len("Terraria"))+"Terraria" + str(protocol)
		sys.stdout.flush()
		packet = chr(0x01) + data
		packlen = len(packet) + 2
		header = struct.pack("<h", packlen)
		packet = header + packet
		client.send(packet)

		"""

		packet = Packet1(102)
		packet.send(client)


		#b1 = client.recv(1)
		#b2 = client.recv(1)

		packet_length = client.recv(2)

		packet_length =  struct.unpack("<h", packet_length)[0] - 2

		print packet_length

		#packet_length = struct.unpack("<h", b1+b2)[0] - 2
		data = client.recv(packet_length)
		command = ord(data[0])
		
		print "Length: ", packet_length
		print "Command: ", command
		playerid =  data[1:]
		print "PlayerID: ", ord(data[1:])

		client.close()
	else:
		bot = TerraBot(HOST, name=PLAYERNAME)
		bot.start()
		while threading.active_count() > 0:
			time.sleep(0.1)
