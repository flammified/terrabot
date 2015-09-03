from terrabot import TerraBot

import threading
import sys
import select

if __name__ == "__main__":

    HOST = '127.0.0.1'
    PORT = 7777
    PROTOCOL = 156
    PLAYERNAME = 'Terrabot'

    if len(sys.argv) > 1:
        HOST = sys.argv[1]
    if len(sys.argv) > 2:
        PLAYERNAME = sys.argv[2]
    if len(sys.argv) > 3:
        PORT = sys.argv[3]

    bot = TerraBot(HOST, port=PORT, name=PLAYERNAME, protocol=PROTOCOL)
    bot.start()
    while threading.active_count() > 1:
       pass
