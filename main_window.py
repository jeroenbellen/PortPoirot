from PySide2.QtWidgets import QMainWindow
from main_widget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self, data_provider):
        super().__init__()

        self.setCentralWidget(MainWidget(data_provider))