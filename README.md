# pyqt-transparent-centralwidget-window
PyQt window which can set the QMainWindow as main widget and make central widget of QMainWindow transparent. Simply put, frame with no image.

This is a combination of <a href="https://github.com/yjg30737/pyqt-transparent-window.git">pyqt-transparent-window</a> and <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a>.

I have to say, each code of <b>pyqt-transparent-centralwidget-window, pyqt-transparent-window, pyqt-custom-titlebar-window</b> are kinda similar. So i tried to reduce the redundancy, but so far that attempt is fruitless. I can do it if i want to but i think that will make the module hard to be maintained or improved.

## Requirements
PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-transparent-centralwidget-window.git --upgrade```

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
    example.setMinMaxCloseButton()
    example.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/151266003-49e788a4-bdb9-4dfb-8475-027523774005.png)

