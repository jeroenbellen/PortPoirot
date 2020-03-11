import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider

from filter_widget import FilterWidget
from port_filter_proxy_model import PortFilterProxyModel
from port_table_view import PortTableView    


data_provider = PortDataProvider()

proxy = PortFilterProxyModel()


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(FilterWidget(proxy))

        layout.addWidget(PortTableView(proxy, data_provider.getAllActivePorts()))

        self.setLayout(layout)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setCentralWidget(MainWidget())


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.resize(500, 600)
window.setWindowTitle('Port Poirot')
window.show()
app.exec_()