import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure


class MpWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        fig = Figure()
        fig.patch.set_facecolor("#ffffff")
        self.canvas = FigureCanvas(fig)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
