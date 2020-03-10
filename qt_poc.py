import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.header_labels = ['Ip', 'Port', 'Pid']


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            return self.header_labels[section]
    


data_provider = PortDataProvider()

def map_2_array(line):
    return [line.ip, line.port, line.pid]

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = list(
            map(map_2_array, data_provider.getAllActivePorts())
        )

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.resize(400, 600)
window.setWindowTitle('Port Poirot')
window.show()
app.exec_()