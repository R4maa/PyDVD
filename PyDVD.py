import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

app = QApplication(sys.argv)

window = QMainWindow()

window.setAttribute(Qt.WA_TranslucentBackground, True)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setWindowFlags(Qt.FramelessWindowHint)

label = QLabel(window)
pixmap = QPixmap('logo.png').scaled(300,300, aspectRatioMode=Qt.KeepAspectRatio)
label.setPixmap(pixmap)
label.setGeometry(0, 0, pixmap.width(), pixmap.height())

window.label = label

window.resize(pixmap.width(),pixmap.height())

window.show()
sys.exit(app.exec_())