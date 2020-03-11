from PySide2.QtWidgets import QTableView, QHeaderView
from port_table_model import PortTableModel

class PortTableView(QTableView):
    def __init__(self, filter_proxy, port_lines):
        super().__init__()

        model = PortTableModel(port_lines)
        filter_proxy.setSourceModel(model)

        
        super().setModel(filter_proxy)

        super().horizontalHeader().setStretchLastSection(True) 
        super().horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)