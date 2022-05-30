from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QDoubleSpinBox


class ControlPanel(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        layout = QHBoxLayout()
        x_spinbox = QDoubleSpinBox()
        x_spinbox.setValue(0.0)
        layout.addWidget(QLabel('X = '))        
        layout.addWidget(x_spinbox)

        y_spinbox = QDoubleSpinBox()
        y_spinbox.setValue(0.0)
        layout.addWidget(QLabel('Y = '))        
        layout.addWidget(y_spinbox)

        t_spinbox = QDoubleSpinBox()
        t_spinbox.setValue(0.0)
        layout.addWidget(QLabel('Tension = '))        
        layout.addWidget(t_spinbox)

        b_spinbox = QDoubleSpinBox()
        b_spinbox.setValue(0.0)
        layout.addWidget(QLabel('Bias = '))        
        layout.addWidget(b_spinbox)

        c_spinbox = QDoubleSpinBox()
        c_spinbox.setValue(0.0)
        layout.addWidget(QLabel('Continuity = '))        
        layout.addWidget(c_spinbox)

        self.setLayout(layout)
