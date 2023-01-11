import sys
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "МАШИНКА"
        self.setWindowTitle(self.title)
        self.images = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png']
        self.setMouseTracking(True)
        self.label = QLabel(self)
        self.pixmap = QPixmap(random.choice(self.images))
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(100, 100,
                               self.pixmap.width(),
                               self.pixmap.height())
        self.resize(self.pixmap.width() * 4, self.pixmap.height() * 4)
        self.resize(500, 500)

    def keyPressEvent(self, event):
        k = event.key()
        super().keyPressEvent(event)
        if k == 32:
            self.pixmap = QPixmap(random.choice(self.images))
            self.label.setPixmap(self.pixmap)

    def mouseMoveEvent(self, event):
        if event.x() + self.pixmap.width() + 5 < 500 and \
                event.y() + self.pixmap.height() + 5 < 500:
            self.label.move(event.x(), event.y())


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
