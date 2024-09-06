from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow
from pyqt_custom_titlebar_window.customTitlebarWindow import CustomTitlebarWindow


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
        if self.isFullScreen():
            pen = QPen(QColor(0, 0, 0, 0), self._margin * 2)
            painter.setPen(pen)
            painter.drawRect(self.rect())
        else:
            # for menu bar only main window
            color = self.getFrameColor()
            # set the border color as same as menu bar color
            pen = QPen(QColor(color), self._margin * 2)
            painter.setPen(pen)
            painter.drawRect(self.rect())
        return super().paintEvent(e)
