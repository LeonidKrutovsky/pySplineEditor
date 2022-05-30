from dataclasses import dataclass
from PyQt5.QtCore import QPointF, QPoint


@dataclass
class Knot:
    pos: QPointF
    tension: float = 0.0
    bias: float = 0.0
    continuity: float = 0.0

    def __init__(self, pos: QPoint):
        self.pos = QPointF(pos)
