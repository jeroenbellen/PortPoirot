
class NetworkConnection():

	def __init__(self, ip, port, pid, process_name = ''):
		self.ip = ip
		self.port = port
		self.pid = pid
		self.process_name = process_name

	def __str__(self):
		return 'Connection=[' + str(self.ip) + ':' + str(self.port) + '], Pid=[' + str(self.pid) + ']'