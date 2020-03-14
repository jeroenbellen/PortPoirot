import psutil
import os
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton
from elevate import elevate

class TableActionButtons(QWidget):

	def __init__(self, port_table_view):
		super().__init__()
		self.port_table_view = port_table_view

		layout = QHBoxLayout()

		btn_kill = QPushButton("Kill selected rows")
		btn_kill.clicked.connect(self._btn_kill_clicked)
		layout.addWidget(btn_kill)

		btn_refresh = QPushButton("Refresh table")
		btn_refresh.clicked.connect(self._btn_refresh_clicked)
		layout.addWidget(btn_refresh)
		
		if psutil.LINUX and os.getuid() != 0:
			btn_make_root = QPushButton("Run as root")
			btn_make_root.clicked.connect(self._btn_make_root_clicked)
			layout.addWidget(btn_make_root)

		layout.addStretch()
		self.setLayout(layout)

	def _btn_kill_clicked(self):
		for pid in self.port_table_view.selected_pids():
			try:
				if pid:
					psutil.Process(pid).kill()
			except psutil.NoSuchProcess:
				pass

		self.port_table_view.refresh_table()

	def _btn_refresh_clicked(self):
		self.port_table_view.refresh_table()

	def _btn_make_root_clicked(self):
		elevate(graphical = False)
