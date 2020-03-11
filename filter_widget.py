from PySide2.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout

class FilterWidget(QWidget):

    def __init__(self):
        super().__init__()

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

    def btn_filter_clicked(self):
        print(self.edit_ip.text())
        print(self.edit_port.text())
        print(self.edit_pid.text())