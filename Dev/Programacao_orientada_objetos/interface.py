from PyQt6.QtWidgets import *
import sys


class tela_Principal(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(270, 220, 480, 320)
        self.setWindowTitle('The libert')
        #self.setFixedSize(self.size())
        self.show()


qt = QApplication(sys.argv)
app = tela_Principal()
sys.exit(qt.exec())

