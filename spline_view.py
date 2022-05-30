from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QMouseEvent, QBrush, QPalette
from PyQt5.QtCore import Qt, pyqtSignal

from spline import Knot, Spline


class SplineView(QWidget):
    current_knot_changed = pyqtSignal(Knot)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.spline = Spline()
        self.cur_knot_index = 0

    def paintEvent(self, _):
        bg_color = self.palette().color(QPalette.Base)
        curve_color = self.palette().color(QPalette.Foreground)

        painter = QPainter(self)
        painter.fillRect(self.rect(), bg_color)

        painter.setPen(QPen(curve_color, 2, Qt.SolidLine))
        painter.setRenderHints(QPainter.HighQualityAntialiasing)
        painter.drawPolyline(self.spline.get_curve())
        painter.setBrush(QBrush(curve_color, Qt.SolidPattern))

        for index, knot in enumerate(self.spline.get_knots()):
            radius = 5 if index == self.cur_knot_index else 3           
            painter.drawEllipse(knot.pos, radius, radius)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        index = self.spline.find_knot_by_pos(event.pos())
        if index is not None:
            self.cur_knot_index = index
        else:
            self.cur_knot_index = len(self.spline.get_knots())      
            self.spline.add_knot(Knot(event.pos()))

        self.current_knot_changed.emit(self.spline.get_knots()[self.cur_knot_index])
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:        
        return super().mouseMoveEvent(event)

    def clear(self):
        self.spline = Spline()
        self.update()

    def set_current_knot(self, knot: Knot):
        self.spline.set_knot(self.cur_knot_index, knot)
        self.update()
