import sys
import random

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.pushButton.clicked.connect(self.clicker)
        self.ev = False

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.pushButton = QPushButton('Нарисовать', self)
        self.pushButton.move(200, 400)
    def paintEvent(self, event):
        if self.ev:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def clicker(self):
        self.ev = True
        self.update()

    def draw(self, qp):
        self.ev = True
        clr = QColor(random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))
        qp.setBrush(clr)
        a = random.randint(10, self.width() // 2)
        qp.drawEllipse(random.randint(self.width() // 2, self.width()) - a,
                       random.randint(self.width() // 2, self.width()) - a, 2 * a, 2 * a)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
