import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt

from port_data_provider import PortDataProvider

from filter_widget import FilterWidget

class SortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, *args, **kwargs):
        QtCore.QSortFilterProxyModel.__init__(self, *args, **kwargs)
        self.filters = {}

    def setFilterByColumn(self, regex, column):
        self.filters[column] = regex
        self.invalidateFilter()

    def clearFilters(self):
        self.filters = {}
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        for key, regex in self.filters.items():
            index = self.sourceModel().index(source_row, key, source_parent)
            if index.isValid():
                text = self.sourceModel().data(index, QtCore.Qt.DisplayRole)
                if not regex in str(text):
                    return False
        return True


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

proxy = SortFilterProxyModel()

class PortTableView(QtWidgets.QTableView):
    def __init__(self):
        super().__init__()

        data = list(
            map(map_2_array, data_provider.getAllActivePorts())
        )

        model = TableModel(data)
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