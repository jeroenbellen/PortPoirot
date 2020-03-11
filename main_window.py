from PySide2.QtWidgets import QMainWindow
from main_widget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self, port_lines):
        super().__init__()

        self.setCentralWidget(MainWidget(port_lines))