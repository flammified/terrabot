#import terrabot.bot
import socket
import struct
import sys

if (__name__ == "__main__"):
	#bot = bot.Bot(server="127.0.0.1")
	HOST = '127.0.0.1'
	PORT = 7777
	ADDR = (HOST, PORT)
	protocol = 102
	sys.stdout.flush()
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	data = chr(len(str(protocol)) + len("Terraria"))+"Terraria" + str(protocol)
	sys.stdout.flush()
	packet = chr(0x01) + data
	packlen = len(packet) + 2
	header = struct.pack("<h", packlen)
	packet = header + packet
	client.send(packet)

	b1 = client.recv(1)
	b2 = client.recv(1)
	packet_length = struct.unpack("<h", b1+b2)[0] - 2
	data = client.recv(packet_length)
	command = ord(data[0])
	
	print "Length: ", packet_length
	print "Command: ", command
	playerid =  data[1:]
	print "PlayerID: ", ord(data[1:])

	client.close()
