from PyQt5.QtWidgets import QMainWindow, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from spline_view import SplineView
from control_panel import ControlPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.spline_view = SplineView()
        self.setCentralWidget(self.spline_view)
        self._create_menubar()
        control_panel = ControlPanel(self.maximumWidth(), self.maximumHeight())
        self.statusBar().addWidget(control_panel)
        self.spline_view.current_knot_changed.connect(control_panel.set_state)
        control_panel.state_changed.connect(self.spline_view.set_current_knot)

    def _create_menubar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")

        clear = file_menu.addAction("Clear")
        clear.triggered.connect(self.spline_view.clear)

        close = file_menu.addAction("&Close")
        close.triggered.connect(self.close)
