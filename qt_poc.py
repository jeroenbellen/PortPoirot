import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider
from main_widget import MainWidget



data_provider = PortDataProvider()




class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainWidget(data_provider.getAllActivePorts()))


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.resize(500, 600)
window.setWindowTitle('Port Poirot')
window.show()
app.exec_()