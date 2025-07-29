import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel

# init main application 
app = QApplication(sys.argv)

window = QMainWindow()  # widget of main service

window.setAttribute(Qt.WA_TranslucentBackground, True)
window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setWindowFlags(Qt.FramelessWindowHint)

label = QLabel(window)
pixmap = QPixmap('logo.png').scaled(300,300, aspectRatioMode=Qt.KeepAspectRatio) # scales image to 300 px while keeping aspect ratio
label.setPixmap(pixmap)
label.setGeometry(0, 0, pixmap.width(), pixmap.height())

window.label = label

window.resize(pixmap.width(),pixmap.height())

window.show()
app.exec()