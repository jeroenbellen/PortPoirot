from network_connection import NetworkConnection

class NetworkConnectionBuilder():

	# Translates the output of psutil.net_connections to an instance of NetworkConnection
	def build(self, raw_input):
		return NetworkConnection(
			ip = raw_input.laddr.ip,
			port = raw_input.laddr.port,
			pid = raw_input.pid
	)