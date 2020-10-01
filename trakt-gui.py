#!/usr/bin/python3
# 
import sys
# Layouts
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget

from UI.Dash import DashUI
from UI.Login import LoginUI
from UI.Search import SearchUI

import json

from PyQt5.QtGui import QIcon, QPixmap

class TraktGui(QMainWindow):
    def __init__(self, parent=None):
        super(TraktGui, self).__init__(parent)
        self.setMinimumSize(1200, 600)
        self.showMaximized()
        self.startDashUI()
        self.startSearchUI()


    def startDashUI(self):
        self.Dash = DashUI(self)

        self.setWindowTitle("Trakt DashBoard")
        self.setCentralWidget(self.Dash)

        self.Dash.SearchBtn.clicked.connect(self.startSearchUI)
        self.Dash.LoginBtn.clicked.connect(self.startLoginUI)
        self.show()

        
    def startLoginUI(self):
        self.Login = LoginUI(self)
        self.setWindowTitle("Trakt Login")
        self.setCentralWidget(self.Login)
        self.Login.BackBtn.clicked.connect(self.startDashUI)
        self.show()


    def startSearchUI(self):
        self.Search = SearchUI(self)
        self.setWindowTitle("Search")
        self.setCentralWidget(self.Search)
        self.Search.BackBtn.clicked.connect(self.startDashUI)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TraktGui()
    sys.exit(app.exec_())