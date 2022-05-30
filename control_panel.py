from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox
from PyQt5.QtCore import QPoint

from knot import Knot


class ControlPanel(QWidget):
    state_changed = pyqtSignal(Knot)

    def __init__(self, width: float, height: float, parent = None):
        super().__init__(parent)
        self.state = Knot(QPoint())

        layout = QHBoxLayout()
        self.x_spinbox = QDoubleSpinBox()
        self.x_spinbox.setValue(0.0)
        self.x_spinbox.setSingleStep(10)
        self.x_spinbox.setMaximum(width)
        self.x_spinbox.valueChanged.connect(self._update_x)
        layout.addWidget(QLabel('X = '))    
        layout.addWidget(self.x_spinbox)

        self.y_spinbox = QDoubleSpinBox()
        self.y_spinbox.setValue(0.0)
        self.y_spinbox.setSingleStep(10)
        self.y_spinbox.setMaximum(height)
        self.y_spinbox.valueChanged.connect(self._update_y)
        layout.addWidget(QLabel('Y = '))
        layout.addWidget(self.y_spinbox)

        def create_spinbox(name: str, slot) -> QDoubleSpinBox:
            spinbox = QDoubleSpinBox()
            spinbox.setValue(0.0)
            spinbox.setSingleStep(0.2)
            spinbox.setRange(-10, 10)
            spinbox.valueChanged.connect(slot)
            layout.addWidget(QLabel(name))        
            layout.addWidget(spinbox)
            return spinbox

        self.t_spinbox = create_spinbox('Tension = ', self._update_tension)
        self.b_spinbox = create_spinbox('Bias = ', self._update_bias) 
        self.c_spinbox = create_spinbox('Continuity = ', self._update_bias) 

        self.setLayout(layout)

    def _update_x(self, value: float):
        if value == self.state.pos.x():
            return
        self.state.pos.setX(value)
        self.state_changed.emit(self.state)

    def _update_y(self, value: float):
        if value == self.state.pos.y():
            return
        self.state.pos.setY(value)
        self.state_changed.emit(self.state)

    def _update_tension(self, value: float):
        if value == self.state.tension:
            return
        self.state.tension = value
        self.state_changed.emit(self.state)

    def _update_bias(self, value: float):
        if value == self.state.bias:
            return
        self.state.bias = value
        self.state_changed.emit(self.state)

    def _update_continuity(self, value: float):
        if value == self.state.continuity:
            return
        self.state.continuity = value
        self.state_changed.emit(self.state)

    def set_state(self, knot: Knot):
        self.state = knot
        self.x_spinbox.setValue(knot.pos.x())
        self.y_spinbox.setValue(knot.pos.y())
        self.t_spinbox.setValue(knot.tension)
        self.b_spinbox.setValue(knot.bias)
        self.c_spinbox.setValue(knot.continuity)
