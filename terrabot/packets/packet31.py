import struct


class Packet31Parser(object):

	def parse(self, world, player, data, ev_man):
		player.x = world.spawnx
		player.y = world.spawny
