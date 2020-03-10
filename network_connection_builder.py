from network_connection import NetworkConnection

class NetworkConnectionBuilder():

	# Translates the output of psutil.net_connections to an instance of NetworkConnection
	def build(self, raw_input):
		return NetworkConnection(
			ip = raw_input[3][0],
			port = raw_input[3][1],
			pid = raw_input[6]
		)