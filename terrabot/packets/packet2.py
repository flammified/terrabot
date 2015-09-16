from terrabot.events.events import Events

class Packet2Parser(object):

    def parse(self, world, player, data, ev_man):
        ev_man.raise_event(Events.Blocked, str(data[2:], 'utf-8'))
