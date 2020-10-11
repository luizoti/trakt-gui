from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QCursor

from PyQt5.QtWidgets import QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QToolButton
from PyQt5.QtWidgets import QWidget, QListView, QListWidget, QListWidgetItem

from API.search import Search



class CustonWidgetItem(QWidget):
    def __init__ (self, _size, cover):
        QWidget.__init__(self)
        self.IcoBar = QHBoxLayout()
        self.addToWatched = QToolButton()
        self.addToWatched.setFixedSize(QSize(30, 30))

        self.addToCollection = QToolButton()
        self.addToCollection.setFixedSize(QSize(30, 30))

        self.addToList = QToolButton()
        self.addToList.setFixedSize(QSize(30, 30))

        self.setHate = QToolButton()
        self.setHate.setFixedSize(QSize(30, 30))
        
        self.addToCollection.clicked.connect(self.test1)
        self.addToList.clicked.connect(self.test2)
        self.setHate.clicked.connect(self.test3)
        self.addToWatched.clicked.connect(self.test4)

        self.IcoBar.addWidget(self.addToCollection)
        self.IcoBar.addWidget(self.addToList)
        self.IcoBar.addWidget(self.setHate)
        self.IcoBar.addStretch(1)
        self.IcoBar.addStretch(1)
        self.IcoBar.addWidget(self.addToWatched)        
        # 
        self.coverwidt = QVBoxLayout()
        self.coverlabel = QLabel()
        cover = QPixmap(cover)
        cover.scaled(_size)
        self.coverlabel.setFixedSize(_size)
        self.coverlabel.setContentsMargins(1, 1, 1, 1) # left, top, right, bottom
        self.coverlabel.setPixmap(cover)
        self.coverlabel.setScaledContents(True)

        self.coverwidt.addWidget(self.coverlabel)

        self.icos = QVBoxLayout()

        self.icos.addLayout(self.coverwidt)
        self.icos.addLayout(self.IcoBar)

        self.icos.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.icos)


    def test1(self):
        print(id(self))
        pass

    def test2(self):
        print(id(self))
        pass

    def test3(self):
        print(id(self))
        pass

    def test4(self):
        print(id(self))
        pass


class CustomList(QListWidget):
    def __init__ (self):
        QListWidget.__init__(self)
        self.setSpacing(1)
        self.setViewMode(QListView.IconMode)
        self.setMovement(QListView.Static)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setResizeMode(QListView.Adjust)


class CustonLineEdit(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)
        self.setPlaceholderText('Pesquise um titulo!')
        self.SearchBtnInside = QToolButton()
        self.SearchBtnInside.setStyleSheet("");
        self.SearchBtnInside.setIcon(QIcon(r"/media/luiz/HD/posinstall/repos/folderfromselected/icos/find.svg"))
        self.SearchBtnInside.setCursor(Qt.ArrowCursor)
        self.lay = QHBoxLayout()
        self.lay.addStretch(1)
        self.lay.addWidget(self.SearchBtnInside)
        self.setText('avengers')
        self.setLayout(self.lay)


class SizeSlider(QSlider):
    def __init__(self):
        QSlider.__init__(self, Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(4)
        self.setValue(0)
        self.setTickPosition(QSlider.TicksBelow)
        self.setTickInterval(1)
        
        
class SearchUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.cover = "/home/luiz/trakt-gui-project/trakt-gui/media/covertest.jpg"
        self.modeState = 1
        self.globalInitialItemSize = QSize(150, 225)
        # Layouts
        self.PHLayList = QHBoxLayout()
        self.VLayTop = QVBoxLayout()
        # 
        self.SearchTextBox = CustonLineEdit()
        self.SearchList = CustomList()
        self.ChangeListModeButton = QPushButton("Mudar modo da lista", self)
        self.ChangeSelectionModeBtn = QPushButton("Ativar Mult Seleção", self)
        self.ReturnToDashboard = QPushButton('Trakt Dashboard', self)
        self.SizeSlider = SizeSlider()

        self.SizeSlider.valueChanged.connect(self.SlideChangeSize)
        self.SearchList.itemSelectionChanged.connect(lambda: self.index())
        # 
        self.ChangeListModeButton.clicked.connect(lambda: self.doChangeListModeButton())
        self.ChangeSelectionModeBtn.clicked.connect(lambda: self.ChangeSelectionMode())
        self.SearchTextBox.SearchBtnInside.clicked.connect(lambda: self.doSearch(self.globalInitialItemSize))
        # 
        self.VLayTop.addWidget(self.SearchTextBox)
        self.VLayTop.addWidget(self.ChangeListModeButton)
        self.VLayTop.addWidget(self.SizeSlider)
        self.VLayTop.addStretch(1)
        self.VLayTop.addWidget(self.ChangeSelectionModeBtn)
        self.VLayTop.addWidget(self.ReturnToDashboard)
        # 
        # 
        self.PHLayList.addLayout(self.VLayTop)
        self.PHLayList.addWidget(self.SearchList)
        self.setLayout(self.PHLayList)
        self.PHLayList.addWidget(self.SearchList)
        self.setLayout(self.PHLayList)


    def createListItens(self, _size):
        self.mapedListItens = {} # dict to map all list itens

        try:
            for item in self.search_data:
                # instance custon widget item
                CustonItem = CustonWidgetItem(_size, self.cover)
                CustonWitgetItemList = QListWidgetItem(self.SearchList)
                # width + 2 para compensar content margin and height + 30 + 2 para compensar barra de icones e contentmargin
                CustonWitgetItemList.setSizeHint((QSize(_size.width() + 2, _size.height() + 30 + 2)))
                # add custon itens to custon widget list
                self.SearchList.addItem(CustonWitgetItemList)
                self.SearchList.setItemWidget(CustonWitgetItemList, CustonItem)
                # store memory adress reference with id() func
                if id(CustonWitgetItemList) not in self.mapedListItens:
                    self.mapedListItens[id(CustonWitgetItemList)] = item
                    pass
                pass
        except Exception as e:
            raise e
        pass


    def doSearch(self, size):
        textbox = self.SearchTextBox.text()

        if len(textbox) > 0:
            try:
                self.search_data = Search('movie', textbox)
            except Exception as e:
                raise e

            self.SearchList.clear()

            if self.search_data == 0:
                print('not found')
            else:
                self.createListItens(size)
                pass
            pass
        pass


    def SlideChangeSize(self):
        self.SearchList.clear()

        sizesDict = {
                   # 100+ 150+
            0: QSize(150, 225),
            1: QSize(250, 375),
            2: QSize(350, 525),
            3: QSize(450, 675),
            4: QSize(550, 825),
        }
        self.globalInitialItemSize = sizesDict[self.SizeSlider.value()]

        self.createListItens(self.globalInitialItemSize)
        pass


    def doChangeListModeButton(self):
        if self.modeState == 0:
            self.SearchList.setViewMode(QListView.IconMode)
            self.modeState = 1
        elif self.modeState == 1:
            self.SearchList.setViewMode(QListView.ListMode)
            self.modeState = 0
            pass
        pass


    def ChangeSelectionMode(self):
        current = self.SearchList.selectionMode()
        if current == 1:
            self.SearchList.setSelectionMode(3)
        elif current == 3:
            self.SearchList.setSelectionMode(1)
            pass
        pass


    def index(self):
        # id of current selected item in list
        _id = self.SearchList.currentRow()
        # get the obj reference of item of list
        obj = self.SearchList.item(_id)
        # print data from item stored in self.mapedListItens with id()
        print(self.mapedListItens[id(obj)])