from . import packets
from . import client

from terrabot.data.player import Player
from terrabot.data.world import World
from terrabot.util.worlddrawer import draw_world
from . import events


class TerraBot(object):
    """A class that handles basic functions of a terraria bot like movement and login"""

    # Defaults to 7777, because that is the default port for the server
    def __init__(self, ip, port=7777, protocol=156, name="Terrabot"):
        super(TerraBot, self).__init__()

        self.protocol = protocol

        self.world = World()
        self.player = Player(name)
        self.evman = events.EventManager()

        self.client = client.Client(ip, port, self.player, self.world, self.evman)

        self.evman.method_on_event(events.Events.PlayerID, self.received_player_id)
        self.evman.method_on_event(events.Events.Initialized, self.initialized)
        self.evman.method_on_event(events.Events.Login, self.logged_in)
        # self.event_manager.method_on_event(events.Events.)

    def start(self):
        self.client.start()
        self.client.add_packet(packets.Packet1(self.protocol))

    def received_player_id(self, event_id, data):
        self.client.add_packet(packets.Packet4(self.player))
        self.client.add_packet(packets.Packet10(self.player))
        self.client.add_packet(packets.Packet2A(self.player))
        self.client.add_packet(packets.Packet32(self.player))
        for i in range(0, 83):
            self.client.add_packet(packets.Packet5(self.player, i))
        self.client.add_packet(packets.Packet6())

    def initialized(self, event, data):
        print("init");
        self.client.add_packet(packets.Packet8(self.player, self.world))

    def logged_in(self, event, data):
        self.client.add_packet(packets.PacketC(self.player, self.world))
        self.client.add_packet(packets.Packet19(self.player))

    def message(self, msg):
        self.client.add_packet(packets.Packet19(self.player, msg))

    def get_event_manager(self):
        """Getter for the event_manager. Hides the internal name so it can be changed"""
        return self.evman
