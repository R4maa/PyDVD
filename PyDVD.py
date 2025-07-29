import sys
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.label = QLabel(self)
        pixmap = QPixmap('logo.png').scaled(
            300, 300, 
            aspectRatioMode=Qt.KeepAspectRatio
        )
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())

    def move(self):
        screen = QApplication.desktop().availableGeometry()
        startdir = random.randrange(1, 360)

        x, y = self.x, self.y

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()