from PySide2.QtWidgets import QWidget, QVBoxLayout
from port_table_view import PortTableView    
from filter_widget import FilterWidget
from port_filter_proxy_model import PortFilterProxyModel

class MainWidget(QWidget):

    def __init__(self, port_lines):
        super().__init__()
        proxy = PortFilterProxyModel()

        layout = QVBoxLayout()
        layout.addWidget(FilterWidget(proxy))
        layout.addWidget(PortTableView(proxy, port_lines))

        self.setLayout(layout)