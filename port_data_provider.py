import psutil

from network_connection_builder import NetworkConnectionBuilder

class PortDataProvider():

	def __init__(self):
		self.builder = NetworkConnectionBuilder()

	def getAllActivePorts(self):
		# TODO specify kind
		net_connections = psutil.net_connections(kind = "inet")
		net_connections = self._map_list_to_network_connection(net_connections)
		net_connections = self._enrich_list_with_process_name(net_connections)
		return net_connections


	def _map_list_to_network_connection(self, net_connections):
		return list(
			map(self.builder.build, net_connections[:])
		)

	def _enrich_list_with_process_name(self, net_connections):
		return list(
			map(self._enrich_with_process_name, net_connections[:])
		)

	def _enrich_with_process_name(self, net_connection):
		net_connection.process_name = psutil.Process(net_connection.pid).name()
		return net_connection
