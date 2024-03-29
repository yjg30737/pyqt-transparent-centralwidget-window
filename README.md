# pyqt-transparent-centralwidget-window
PyQt window which can set the QMainWindow as main widget and make central widget of QMainWindow transparent. Simply put, frame with no image.

Frame will be removed when full screen is being activated.

This module directly inherits the <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>.

## Requirements
PyQt5 >= 5.15

## Setup
`python -m pip install pyqt-transparent-centralwidget-window`

## Included Package
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a> - Parent widget

## Example
Code Sample
```python
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QApplication
from pyqt_transparent_centralwidget_window import TransparentCentralWidgetWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        menuBar = QMenuBar()
        filemenu = QMenu('File', self)
        menuBar.addMenu(filemenu)
        self.setMenuBar(menuBar)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = TransparentCentralWidgetWindow(MainWindow())
    example.setButtons()
    example.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/151266003-49e788a4-bdb9-4dfb-8475-027523774005.png)

## Example by App
* <a href="https://github.com/yjg30737/pyqt-capturer.git">pyqt-capturer</a>

