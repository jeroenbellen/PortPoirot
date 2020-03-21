from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout

class FilterWidget(QWidget):

    def __init__(self, filter_proxy):
        super().__init__()
        self.filter_proxy = filter_proxy

        layout = QHBoxLayout()

        layout.addWidget(QLabel("Ip"))
        self.edit_ip = QLineEdit("")
        self._set_edit_width(self.edit_ip)
        layout.addWidget(self.edit_ip)

        layout.addWidget(QLabel("Port"))
        self.edit_port = QLineEdit("")
        self._set_edit_width(self.edit_port)
        layout.addWidget(self.edit_port)

        layout.addWidget(QLabel("Pid"))
        self.edit_pid = QLineEdit("")
        self._set_edit_width(self.edit_pid)
        layout.addWidget(self.edit_pid)

        layout.addWidget(QLabel("Process name"))
        self.edit_process_name = QLineEdit("")
        self._set_edit_width(self.edit_process_name)
        layout.addWidget(self.edit_process_name)
        
        btn_filter = QPushButton("Filter")
        btn_filter.clicked.connect(self.btn_filter_clicked)
        layout.addWidget(btn_filter)

        layout.addStretch()
        self.setLayout(layout)

    def _set_edit_width(self, edit):
        edit.setMinimumWidth(100)
        edit.setMaximumWidth(100)

    def filter_on_index(self, edit, index):
        text = edit.text().strip()

        if text:
            self.filter_proxy.setFilterByColumn(text, index)

    def btn_filter_clicked(self):
        self.filter_proxy.clearFilters()
        self.filter_on_index(self.edit_ip, 0)
        self.filter_on_index(self.edit_port, 1)
        self.filter_on_index(self.edit_pid, 2)
        self.filter_on_index(self.edit_process_name, 3)