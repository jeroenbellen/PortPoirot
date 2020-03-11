import sys 
from PySide2.QtWidgets import QApplication
from port_data_provider import PortDataProvider
from main_window import MainWindow

data_provider = PortDataProvider()

app = QApplication(sys.argv)

window = MainWindow(data_provider)

window.resize(500, 600)
window.setWindowTitle('Port Poirot')

window.show()

app.exec_()