import unittest
from network_connection import NetworkConnection

class NetworkConnectionTest(unittest.TestCase):

	def test_init(self):
		nc = NetworkConnection("ip", 8080, 432)

		assert nc.ip == "ip"
		assert nc.port == 8080
		assert nc.pid == 432