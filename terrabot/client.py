import socket
import struct
import threading

from . import packets

class Client(object):
    """A class that handles the connection to a Terraria Server"""

    def __init__(self, HOST, PORT, player, world, event_manager):
        super(Client, self).__init__()

        self.ADDR = (HOST, PORT)
        self.player = player
        self.world = world
        self._evman = event_manager

        self.writeThread = threading.Thread(target=self.read_packets)
        self.writeThread.daemon = True

        self.readThread = threading.Thread(target=self.write_packets)
        self.readThread.daemon = True

        self.running = False

        self.write_queue = []
        self.client = None


    def add_packet(self, packet):
        """Add a packet to the queue"""
        self.write_queue.append(packet)


    def read_packets(self):
        """Read packets from the socket and parse them"""
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
                pass

            if packno == 2:
                self.stop()
                continue

    def write_packets(self):
        """Write packets from the queue"""
        while self.running:
            if len(self.write_queue) > 0:
                self.write_queue[0].send(self.client)
                self.write_queue.pop(0)

    def start(self):
        """Open sockets to the server and start threads"""
        if not self.writeThread.isAlive() and not self.readThread.isAlive():
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)
            self.running = True
            self.writeThread.start()
            self.readThread.start()

    def stop(self):
        """Stop the client"""
        self.running = False
