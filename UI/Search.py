from PyQt5.QtWidgets import QPushButton, QToolButton
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget, QListView
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel

from PyQt5.QtCore import QSize, Qt
from PyQt5.Qt import QAbstractItemView
# https://stackoverflow.com/questions/60074092/pyqt5-qlistwidget-custom-items

movies = [{
            "type": "movie",
            "score": 13.581132,
            "movie": {
              "title": "The Little Rascals",
              "year": 1994,
              "ids": {
                "trakt": 6051,
                "slug": "the-little-rascals-1994",
                "imdb": "tt0110366",
                "tmdb": 10897
              }
            }
          },
          {
            "type": "movie",
            "score": 10.858086,
            "movie": {
              "title": "The Little Rascals Save the Day",
              "year": 2014,
              "ids": {
                "trakt": 159646,
                "slug": "the-little-rascals-save-the-day-2014",
                "imdb": "tt2490004",
                "tmdb": 260535
              }
            }
          }]


class QCustomQWidget(QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.setMinimumSize(150, 250)
        self.PrimaryWidget = QVBoxLayout()
        self.ImageWidget   = QVBoxLayout()
        self.IcoBar        = QHBoxLayout()

        self.PrimaryWidget.addLayout(self.ImageWidget)
        self.PrimaryWidget.addLayout(self.IcoBar)
        coverlabel = QLabel(self)
        cover = QPixmap('/home/luiz/6e55f1ab23.jpg')
        cover = cover.scaled(150, 250, Qt.KeepAspectRatio,transformMode=Qt.SmoothTransformation)
        coverlabel.setScaledContents(True)
        coverlabel.setPixmap(cover)


        btn1 = QToolButton()
        btn2 = QToolButton()
        btn3 = QToolButton()
        btn4 = QToolButton()

        self.ImageWidget.addWidget(coverlabel)
        self.IcoBar.addWidget(btn1)
        self.IcoBar.addWidget(btn2)
        self.IcoBar.addWidget(btn3)
        self.IcoBar.addWidget(btn4)
        self.setLayout(self.PrimaryWidget)


class SearchUI(QWidget):
    def __init__(self, parent=None):
        super(SearchUI, self).__init__(parent)
        self.SearchBtn = QPushButton("Search", self)
        self.SearchBtn.setIcon(QIcon(r"/media/luiz/HD/posinstall/repos/folderfromselected/icos/find.svg"))

        self.SelectionModeBtn = QPushButton("Me", self)
        
        self.BackBtn = QPushButton('Back', self)
        self.Custon = QCustomQWidget()
        # Layouts
        self.PHLayList = QHBoxLayout()

        self.VLayTop = QVBoxLayout()
        self.VLayLow = QVBoxLayout()
        self.HLayList = QHBoxLayout()
        # 
        # 
        self.SearchList = QListWidget(self)
        self.SearchList.setViewMode(QListView.IconMode)
        self.SearchList.setMovement(QListView.Static)
        self.SearchList.setFixedSize(800, 650)
        # 
        for item in movies:
            traktid = item['movie']['ids']['trakt']
            self.myQCustomQWidget = QCustomQWidget()
            self.myQListWidgetItem = QListWidgetItem(self.SearchList)  # QtWidgets
            # Set size hint
            self.myQListWidgetItem.setSizeHint(self.myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.SearchList.addItem(self.myQListWidgetItem)
            self.SearchList.setItemWidget(self.myQListWidgetItem, self.myQCustomQWidget)
            pass
            # 


        self.SearchList.itemSelectionChanged.connect(lambda: self.index())
        self.SelectionModeBtn.clicked.connect(lambda: self.ChangeCheck())
        self.VLayTop.addWidget(self.SearchBtn)
        self.VLayTop.addWidget(self.SelectionModeBtn)
        self.VLayLow.addWidget(self.BackBtn)
        self.HLayList.addWidget(self.SearchList)
        # 
        # 
        self.PHLayList.addLayout(self.VLayTop)
        self.PHLayList.addLayout(self.VLayLow)
        self.PHLayList.addLayout(self.HLayList)
        self.setLayout(self.PHLayList)


    def ChangeCheck(self):
        current = self.SearchList.selectionMode()
        if current == 1:
            self.SearchList.setSelectionMode(3)
        elif current == 3:
            self.SearchList.setSelectionMode(1)
            pass
        pass

    def index(self):
        self.SearchList.currentIndex()
        pass