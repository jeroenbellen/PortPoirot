import psutil
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton

class TableActionButtons(QWidget):

	def __init__(self, port_table_view):
		super().__init__()
		self.port_table_view = port_table_view

		layout = QHBoxLayout()
		btn_kill = QPushButton("Kill selected rows")
		btn_kill.clicked.connect(self._btn_kill_clicked)
		layout.addWidget(btn_kill)

		self.setLayout(layout)

	def _btn_kill_clicked(self):
		for pid in self.port_table_view.selected_pids():
			psutil.Process(pid).kill()

		self.port_table_view.refresh_table()
