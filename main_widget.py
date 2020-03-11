from PySide2.QtWidgets import QWidget, QVBoxLayout
from port_table_view import PortTableView    
from filter_widget import FilterWidget
from port_filter_proxy_model import PortFilterProxyModel
from table_action_buttons import TableActionButtons

class MainWidget(QWidget):

    def __init__(self, data_provider):
        super().__init__()
        proxy = PortFilterProxyModel()

        layout = QVBoxLayout()
        layout.addWidget(FilterWidget(proxy))

        port_table_view = PortTableView(proxy, data_provider)
        layout.addWidget(port_table_view)
        layout.addWidget(TableActionButtons(port_table_view))

        self.setLayout(layout)