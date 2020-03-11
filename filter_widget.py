from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout

class FilterWidget(QWidget):

    def __init__(self, filter_proxy):
        super().__init__()
        self.filter_proxy = filter_proxy

        layout = QHBoxLayout()

        layout.addWidget(QLabel("Ip"))
        self.edit_ip = QLineEdit("")
        layout.addWidget(self.edit_ip)

        layout.addWidget(QLabel("Port"))
        self.edit_port = QLineEdit("")
        layout.addWidget(self.edit_port)

        layout.addWidget(QLabel("Pid"))
        self.edit_pid = QLineEdit("")
        layout.addWidget(self.edit_pid)
        
        btn_filter = QPushButton("Filter")
        btn_filter.clicked.connect(self.btn_filter_clicked)
        layout.addWidget(btn_filter)

        self.setLayout(layout)

    def filter_on_index(self, edit, index):
        text = edit.text().strip()

        if text:
            self.filter_proxy.setFilterByColumn(text, index)

    def btn_filter_clicked(self):
        self.filter_proxy.clearFilters()
        self.filter_on_index(self.edit_ip, 0)
        self.filter_on_index(self.edit_port, 1)
        self.filter_on_index(self.edit_pid, 2)