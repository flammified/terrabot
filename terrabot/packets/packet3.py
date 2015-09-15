from terrabot.events import Events

class Packet3Parser(object):

    def parse(self, world, player, data, ev_man):
        player.playerID = ord(data[1:])
        ev_man.raise_event(Events.PlayerID, player.playerID)
