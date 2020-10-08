#!/usr/bin/python3
# 
import pylint
import json
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QDesktopWidget

from UI.Dash import DashUI
from UI.Login import LoginUI
from UI.Search import SearchUI

from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from os.path import dirname, join


class CurrentResolution(QDesktopWidget):
    def __init__(self):
        QDesktopWidget.__init__(self)
        self.screenGeometry(-1)
        self.height()
        self.width()


class TraktGui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.CurrentDir = dirname(__file__)
        self.resolution = CurrentResolution()
        self.Dash = DashUI()
        self.Login = LoginUI()
        self.Search = SearchUI()
        # self.setStyleSheet(open(join(self.CurrentDir ,'UI' ,'stylesheet.css'),"r").read())
        self.showMaximized()
        # self.startDashUI()
        self.startSearchUI()


    def startDashUI(self):
        self.Dash = DashUI()
        self.setWindowTitle("Trakt DashBoard")
        self.setCentralWidget(self.Dash)

        self.Dash.SearchBtn.clicked.connect(self.startSearchUI)
        self.Dash.SearchBtn.clicked.connect(self.resizeEvent)
        self.Dash.LoginBtn.clicked.connect(self.startLoginUI)
        self.show()

        
    def startLoginUI(self):
        self.Login = LoginUI()
        self.setWindowTitle("Trakt Login")
        self.setCentralWidget(self.Login)
        self.Login.ReturnToDashboard.clicked.connect(self.startDashUI)
        self.show()


    def startSearchUI(self):
        self.Search = SearchUI()
        self.setWindowTitle("Search")
        self.setCentralWidget(self.Search)
        self.Search.ReturnToDashboard.clicked.connect(self.startDashUI)
        self.show()


    def resizeEvent(self, event):
        print('Resolução:', self.resolution.width(), self.resolution.height(), '-', 'Janela:', 'WIDTH:', self.width(), 'HEIGHT:', self.height())
        # 1366
        if self.resolution.width() <= 1366 and self.resolution.height() <= 768:
            _size = 180
            self.setMinimumSize(QSize(770, 520))
            # maximizado
            # 1366 HEIGHT: 702
            if 1350 < self.width() < 1370 and 690 < self.height() < 710:
                _size = 264
                pass
                        
            if 650 < self.width() < 680 or 700 > self.width() > 660 and 320 < self.height() < 340:
                _size = 180
                pass
            
            if 700 > self.width() > 660 and 320 < self.height() < 340:
                _size = 180
                pass
        # 1080
        elif self.resolution.width() <= 1920 and self.resolution.height() <= 1080:
            self.setMinimumSize(QSize(952, 520))
            _size = 310 # minimo
            if self.width() <= 920 and 510 < self.height() < 530:
                # Caso a janela seja movida e não esteja dockada
                # WIDTH: 950 HEIGHT: 520
                _size = 310 # minimo
                pass

            if 1800 < self.width() <= 1920 and 1000 < self.height() < 1020:
                # maximizado
                _size = 380
                pass

            if 940 < self.width() < 960:
                # WIDTH: 952
                if 990 < self.height() < 1010 or 470 < self.height() < 490:
                    # HEIGHT: 1009
                    # Janela dividida verticalmente
                    # HEIGHT: 487
                    # Janela dividida verticalmente e horizontal
                    _size = 310
                    pass
            elif 1910 < self.width() < 1920:
                # WIDTH: 1912
                # Janela dividida horizontal
                _size = 370
                pass
            
        self.Search.ChangeListModeButton.setFixedWidth(_size)
        self.Search.SizeSlider.setFixedWidth(_size)
        self.Search.ChangeSelectionModeBtn.setFixedWidth(_size)
        self.Search.ReturnToDashboard.setFixedWidth(_size)
        self.Search.SearchTextBox.setFixedWidth(_size)
        pass


if __name__ == '__main__':
    QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QtWidgets.QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    MainEventThread = QApplication([])
    MainApp = TraktGui()
    MainApp.show()
    MainEventThread.exec()