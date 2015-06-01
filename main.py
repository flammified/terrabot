from terrabot import TerraBot

import threading, time
import sys
import select

if (__name__ == "__main__"):

	HOST = '127.0.0.1'
	PORT = 7777
	PROTOCOL = 102
	PLAYERNAME = 'Terrabot'

	if (len(sys.argv) > 1):
		HOST = sys.argv[1]
	if (len(sys.argv) > 2):
		PLAYERNAME = sys.argv[2]
	if (len(sys.argv) > 3):
		PORT = sys.argv[3]

	bot = TerraBot(HOST, port=PORT, name=PLAYERNAME)
	bot.start()
	while threading.active_count() > 1:
		while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
			line = sys.stdin.readline()
			if line:
				bot.message(line.rstrip())
