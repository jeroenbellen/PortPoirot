import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider
from main_window import MainWindow


data_provider = PortDataProvider()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow(data_provider.getAllActivePorts())
window.resize(500, 600)
window.setWindowTitle('Port Poirot')
window.show()
app.exec_()