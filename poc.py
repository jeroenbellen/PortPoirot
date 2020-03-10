import psutil

net_connections = psutil.net_connections(kind = "inet")

for nc in net_connections:
	print(str(nc[3][0]) + ' : ' + str(nc[3][1]) + "/t pid: " + str(nc[6]))


print('-----------------')
print(net_connections[0])

from network_connection import NetworkConnection
from network_connection_builder import NetworkConnectionBuilder

builder = NetworkConnectionBuilder()
r = list(map(builder.build, net_connections[:]))

print(r[0])