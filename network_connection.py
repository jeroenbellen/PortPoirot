
class NetworkConnection():

	def __init__(self, ip, port, pid):
		self.ip = ip
		self.port = port
		self.pid = pid

	def __str__(self):
		return 'Connection=[' + str(self.ip) + ':' + str(self.port) + '], Pid=[' + str(self.pid) + ']'