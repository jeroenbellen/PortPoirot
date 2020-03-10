import psutil

from network_connection_builder import NetworkConnectionBuilder

class PortDataProvider():

	def __init__(self):
		self.builder = NetworkConnectionBuilder()

	def getAllActivePorts(self):
		# TODO specify kind
		net_connections = psutil.net_connections(kind = "inet")

		return list(
			map(self.builder.build, net_connections[:])
		)
