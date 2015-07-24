class Packet3Parser(object):

    def parse(self, world, player, data):
        player.playerID = ord(data[1:])
        print "PlayerID: " + str(player.playerID)
