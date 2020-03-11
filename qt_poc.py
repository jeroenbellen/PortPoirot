import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider

from filter_widget import FilterWidget
from port_filter_proxy_model import PortFilterProxyModel
from port_table_model import PortTableModel
    


data_provider = PortDataProvider()

proxy = PortFilterProxyModel()

class PortTableView(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()

        model = PortTableModel(data_provider.getAllActivePorts())
        proxy.setSourceModel(model)

        
        super().setModel(proxy)

        super().horizontalHeader().setStretchLastSection(True) 
        super().horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(FilterWidget(proxy))
        layout.addWidget(PortTableView())

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