import socket
import struct
import threading
from . import packets

from terrabot.data.player import Player
from terrabot.data.world import World
from terrabot.util.worlddrawer import draw_world
from .events import Events, EventManager


class TerraBot(object):
    """A bot for a terraria server"""

    # Defaults to 7777, because that is the default port for the server
    def __init__(self, ip, port=7777, protocol=156, name="Terrabot"):
        super(TerraBot, self).__init__()

        self.HOST = ip
        self.PORT = port
        self.ADDR = (self.HOST, self.PORT)

        self.protocol = protocol
        self.running = False

        self.writeThread = threading.Thread(target=self.read_packets)
        self.writeThread.daemon = True

        self.readThread = threading.Thread(target=self.write_packets)
        self.readThread.daemon = True

        self.client = None
        self.writeQueue = []

        self.world = World()
        self.player = Player(name)
        self._evman = EventManager()

        self._evman.method_on_event(Events.PlayerID, self.received_player_id)
        self._evman.method_on_event(Events.Initialized, self.initialized)
        self._evman.method_on_event(Events.Login, self.logged_in)
        # self.event_manager.method_on_event(events.Events.)


    """Connects to the server and starts the main loop"""
    def start(self):
        if not self.writeThread.isAlive() and not self.readThread.isAlive():
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)
            self.running = True
            self.writeThread.start()
            self.readThread.start()
            self.add_packet(packets.Packet1(self.protocol))


    def read_packets(self):
        while self.running:
            packet_length = self.client.recv(2)
            if len(packet_length) < 2:
                self.stop()
                continue
            packet_length = struct.unpack("<h", packet_length)[0] - 2

            data = self.client.recv(packet_length)
            packno = data[0]

            try:
                parser = "Packet" + format(packno, 'x').upper() + "Parser"
                packet_class = getattr(packets, parser)
                packet_class().parse(self.world, self.player, data, self._evman)
            except AttributeError as e:
                pass #SILENCES ERRORS!

            if packno == 2:
                self.stop()
                continue

    def item_owner_changed(self, id, data):
        if self.player.logged_in:
            self.add_packet(packets.Packet16(data[0], data[1]))

    def received_player_id(self, event_id, data):
        self.add_packet(packets.Packet4(self.player))
        self.add_packet(packets.Packet10(self.player))
        self.add_packet(packets.Packet2A(self.player))
        self.add_packet(packets.Packet32(self.player))
        for i in range(0, 83):
            self.add_packet(packets.Packet5(self.player, i))
        self.add_packet(packets.Packet6())

    def initialized(self, event, data):
        self.add_packet(packets.Packet8(self.player, self.world))

    def logged_in(self, event, data):
        self.add_packet(packets.PacketC(self.player, self.world))
        self.add_packet(packets.Packet19(self.player))
        self._evman.method_on_event(Events.ItemOwnerChanged, self.item_owner_changed)

    def write_packets(self):
        while self.running:
            if len(self.writeQueue) > 0:
                self.writeQueue[0].send(self.client)
                self.writeQueue.pop(0)

    def teleport(self, x, y):
        self.add_packet(packets.Packet41(self.player.playerID, x, y))

        #Temporary fix until I parse player update data!
        self.player.x = x
        self.player.y = y

    def message(self, msg, color=None):
        if self.player.logged_in:
            if color:
                hex_code = '%02x%02x%02x' % color
                msg = "[c/" + hex_code + ":" + msg + "]"
            self.add_packet(packets.Packet19(self.player, msg))


    """Returns the event manager of this bot
       A function is used, so I can change the name internally without
       affecting bots
       """
    def get_event_manager(self):
        return self._evman

    def add_packet(self, packet):
        self.writeQueue.append(packet)

    def stop(self):
        self.running = False
