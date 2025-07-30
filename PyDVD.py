import sys, random, glob
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

        self.x_speed = 5
        self.y_speed = 5
        self.timer = QTimer()   # use qtimer due to pyqt being event based
        self.timer.timeout.connect(self.moveLogo)
        self.timer.start(16)

    def moveLogo(self):
        screen = QApplication.primaryScreen().availableGeometry()

        x, y = self.x(), self.y()
        new_x = x + self.x_speed
        new_y = y + self.y_speed

        # Bounce horizontally
        if new_x <= 0 or new_x + self.width() >= screen.width():
            self.x_speed *= -1
            new_x = max(0, min(new_x, screen.width() - self.width()))   #check clipping
            self.colorChange()

        # Bounce vertically
        if new_y <= 0 or new_y + self.height() >= screen.height():
            self.y_speed *= -1
            new_y = max(0, min(new_y, screen.height() - self.height())) #check clipping
            self.colorChange()

        self.move(new_x, new_y)

    def colorChange(self):
        images = glob.glob("./logoColors/*.png")
        random_image = random.choice(images)

        newPixmap = QPixmap(random_image).scaled(
            300, 300, 
            aspectRatioMode=Qt.KeepAspectRatio
        )
        
        self.label.setPixmap(newPixmap) # change image

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()