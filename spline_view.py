from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QMouseEvent, QBrush, QPalette
from PyQt5.QtCore import Qt, pyqtSignal

from spline import Knot, Spline


class SplineView(QWidget):
    status_changed = pyqtSignal(str)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.spline = Spline()

    def paintEvent(self, _):
        bg_color = self.palette().color(QPalette.Base)
        curve_color = self.palette().color(QPalette.Foreground)

        painter = QPainter(self)
        painter.fillRect(self.rect(), bg_color)

        painter.setPen(QPen(curve_color, 2, Qt.SolidLine))
        painter.setRenderHints(QPainter.HighQualityAntialiasing)
        painter.drawPolyline(self.spline.get_curve())
        painter.setBrush(QBrush(QColor(182, 219, 73), Qt.SolidPattern))

        for knot in self.spline.get_knots():
            painter.drawEllipse(knot.pos, 3, 3)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.spline.add_knot(Knot(event.pos()))
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        
        return super().mouseMoveEvent(event)

    def clear(self):
        self.spline = Spline()
        self.update()
