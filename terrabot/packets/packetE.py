from terrabot.util.streamer import Streamer

from terrabot.events.events import Events


class PacketEParser(object):
    def parse(self, world, player, data, ev_man):

        #If player is active
        if data[2] == 1:
            #Raise event with player_id
            ev_man.raise_event(Events.NewPlayer, data[1])
