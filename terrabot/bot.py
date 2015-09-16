import socket
import struct
import threading
from . import packets

from terrabot.data.player import Player
from terrabot.data.world import World
from terrabot.util.worlddrawer import draw_world
from . import events


class TerraBot(object):
    """A bot for a terraria server"""

    # Defaults to 7777, because that is the default port for the server
    def __init__(self, ip, port=7777, protocol=155, name="Terrabot"):
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
        self.event_manager = events.EventManager()

        self.event_manager.method_on_event(events.Events.PlayerID, self,  self.received_player_id)


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
                packet_class().parse(self.world, self.player, data, self.event_manager)
            except AttributeError as e:
                pass

            if packno == 11:
                pass
                # draw_world(self.world)

            if packno == 2:
                self.stop()
                continue

            if packno == 3:
                self.add_packet(packets.Packet4(self.player))
                self.add_packet(packets.Packet10(self.player))
                self.add_packet(packets.Packet2A(self.player))
                self.add_packet(packets.Packet32(self.player))
                for i in range(0, 83):
                    self.add_packet(packets.Packet5(self.player, i))
                self.add_packet(packets.Packet6())

            if packno == 7 and not self.player.initialized:
                self.add_packet(packets.Packet8(self.player, self.world))
                self.player.initialized = True

            if packno == 7 and self.player.initialized and not self.player.logged_in:
                self.add_packet(packets.PacketC(self.player, self.world))
                self.add_packet(packets.Packet19(self.player))

    def received_player_id(self, event_id, data):
        pass

    def write_packets(self):
        while self.running:
            if len(self.writeQueue) > 0:
                self.writeQueue[0].send(self.client)
                self.writeQueue.pop(0)

    def message(self, msg):
        self.add_packet(packets.Packet19(self.player, msg))

    def print_hex_array(self, data):
        str = ""
        for i in data:
            str += format(ord(i), "x")
        return str

    def add_packet(self, packet):
        self.writeQueue.append(packet)

    def stop(self):
        self.running = False
