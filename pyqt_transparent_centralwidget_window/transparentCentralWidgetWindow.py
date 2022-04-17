from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow
from pyqt_custom_titlebar_window import CustomTitlebarWindow
from pyqt_top_titlebar_widget import TopTitleBarWidget


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
        widget = self.layout().itemAt(0).widget()
        if isinstance(widget, QMainWindow):
            # set the border color as same as menu bar color
            color = widget.menuBar().palette().color(QPalette.Base)
            pen = QPen(QColor(color), self._margin * 2)
            painter.setPen(pen)
            painter.drawRect(self.rect())
        elif isinstance(widget, TopTitleBarWidget):
            color = self.layout().itemAt(1).widget().menuBar().palette().color(QPalette.Base)
            pen = QPen(QColor(color), self._margin * 2)
            painter.setPen(pen)
            painter.drawRect(self.rect())
            widget.setStyleSheet(f'background-color: {color.name()}')
            widget.setAutoFillBackground(True)
        return super().paintEvent(e)