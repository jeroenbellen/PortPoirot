from PySide2.QtCore import QAbstractTableModel, Qt

class PortTableModel(QAbstractTableModel):

    def __init__(self, port_lines):
        super(PortTableModel, self).__init__()
        self._data = self._map_data(port_lines)
        self.header_labels = ['Ip', 'Port', 'Pid', 'Process Name']


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]

    def _map_data(self, port_lines):
        return list(
            map(self._map_2_array, port_lines)
        )

    def _map_2_array(self, line):
        return [line.ip, line.port, line.pid, line.process_name]