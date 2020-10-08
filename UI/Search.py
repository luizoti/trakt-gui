from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QCursor

from PyQt5.QtWidgets import QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QToolButton
from PyQt5.QtWidgets import QWidget, QListView, QListWidget, QListWidgetItem


from API.search import SearchTrakt


class CustonItem(QWidget):
    def __init__ (self, _size):
        QWidget.__init__(self)
        self.setMinimumSize(_size)

        self.coverlabel = QLabel(self)
        cover = QPixmap('/home/luiz/trakt-gui-project/trakt-gui/media/covertest.jpg')
        self.cover = cover.scaled(_size)
        self.coverlabel.setPixmap(self.cover)

        self.PrimaryWidget = QVBoxLayout()
        self.PrimaryWidget.addWidget(self.coverlabel)
        self.PrimaryWidget.setContentsMargins(1.25, 1.25, 1.25, 1.25)
        self.setLayout(self.PrimaryWidget)


class CustomList(QListWidget):
    def __init__ (self):
        QListWidget.__init__(self)

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
        self.modeState = 1
        self.globalInitialItemSize = QSize(150, 225)

        self.Search = SearchTrakt()
        # Layouts
        self.PHLayList = QHBoxLayout()
        self.VLayTop = QVBoxLayout()
        # 
        self.SearchTextBox = CustonLineEdit()
        self.SearchList = CustomList()
        self.ChangeListModeButton = QPushButton("Mudar modo da lista", self)
        self.ChangeSelectionModeBtn = QPushButton("Me", self)
        self.ReturnToDashboard = QPushButton('Trakt Dashboard', self)
        self.SizeSlider = SizeSlider()

        self.SizeSlider.valueChanged.connect(self.SlideChangeSize)
        self.SearchList.itemSelectionChanged.connect(lambda: self.index())
        # 
        self.ChangeListModeButton.clicked.connect(lambda: self.ChangeChangeListModeButton())
        self.ChangeSelectionModeBtn.clicked.connect(lambda: self.ChangeSelectionMode())
        self.SearchTextBox.SearchBtnInside.clicked.connect(
            lambda: self.doSearch(self.globalInitialItemSize))
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
                tk_id = item['movie']['ids']['trakt']
                # instance custon widget item
                myCustonitem = CustonItem(_size)
                myCustonListItem = QListWidgetItem(self.SearchList)
                myCustonListItem.setSizeHint(_size)
                # add custon itens to custon widget list
                self.SearchList.addItem(myCustonListItem)
                self.SearchList.setItemWidget(myCustonListItem, myCustonitem)
                # store memory adress reference with id() func
                if id(myCustonListItem) not in self.mapedListItens:
                    self.mapedListItens[id(myCustonListItem)] = item
                    pass
                pass
        except Exception as e:
            raise e
        pass


    def doSearch(self, size):
        textbox = self.SearchTextBox.text()

        if len(textbox) > 0:
            try:
                self.search_data = self.Search.Search('movie', textbox)
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
            0: QSize(150, 225),
            1: QSize(250, 375),
            2: QSize(350, 525),
            3: QSize(450, 675),
            4: QSize(550, 825),
        }
        self.globalInitialItemSize = sizesDict[self.SizeSlider.value()]

        self.createListItens(self.globalInitialItemSize)
        pass


    def ChangeChangeListModeButton(self):
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