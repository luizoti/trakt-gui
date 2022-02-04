from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QIcon, QPixmap


class DashUI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.SearchBtn = QPushButton("Search", self) 
        self.SearchBtn.move(200, 350)

        self.LoginBtn = QPushButton("Login Trakt", self)
        self.LoginBtn.move(100, 350)
