from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow
from pyqt_custom_titlebar_window import CustomTitlebarWindow


class TransparentCentralWidgetWindow(CustomTitlebarWindow):
    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        self.__initUi(main_window)

    def __initUi(self, main_window):
        main_window.setAttribute(Qt.WA_TranslucentBackground, True)
        main_window.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)

    def paintEvent(self, e):
        painter = QPainter(self)
        # get the main window
        main_window = self.layout().itemAt(0).widget()
        # set the border color as same as menu bar color
        color = main_window.menuBar().palette().color(QPalette.Base)
        pen = QPen(QColor(color), self._margin * 2)
        painter.setPen(pen)
        painter.drawRect(self.rect())
        return super().paintEvent(e)