import sys 
import useless_process_killer
import psutil
from elevate import elevate
from PySide2.QtWidgets import QApplication
from port_data_provider import PortDataProvider
from main_window import MainWindow

useless_process_killer.check_and_kill()

if psutil.MACOS:
    elevate()

data_provider = PortDataProvider()

app = QApplication(sys.argv)

window = MainWindow(data_provider)

window.resize(500, 600)
window.setWindowTitle('Port Poirot')

window.show()

app.exec_()