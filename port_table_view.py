from PySide2.QtWidgets import QTableView, QHeaderView, QAbstractItemView
from PySide2.QtCore import Qt
from port_table_model import PortTableModel

class PortTableView(QTableView):
    def __init__(self, filter_proxy, data_provider):
        super().__init__()
        self.filter_proxy = filter_proxy
        self.data_provider = data_provider

        model = PortTableModel(data_provider.getAllActivePorts())
        self.filter_proxy.setSourceModel(model)

        
        self.setModel(self.filter_proxy)

        self.horizontalHeader().setStretchLastSection(True) 
       	self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

       	self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def refresh_table(self):
    	model = PortTableModel(self.data_provider.getAllActivePorts())
    	self.filter_proxy.setSourceModel(model)
    	self.setModel(self.filter_proxy)


    def selected_pids(self):

    	return list(
    		map(self._extract_selected_pid, self.selectionModel().selectedRows())
    	)


    def _extract_selected_pid(self, selected_row):
    	row = selected_row.row()
    	return self.model().index(row, 2).data()