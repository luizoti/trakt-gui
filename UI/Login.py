import json

from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QPushButton, QToolButton, QLabel, QLineEdit, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QDesktopWidget, QSlider

from API.login import GetCode, CheckAuth

messege = ['Acesse ', 
            '', 
             ' e autorize o trakt-gui. Usando o codigo abaixo, ',
                ' . O codigo expira em ',
                   '', 
                    ' minutos.']


class LoginUI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.LoginLabelInfo = QLabel(self)
        self.LoginLabelInfo.setOpenExternalLinks(True)
        self.StatusLabel = QLabel(self)
        self.StatusLabel.setStyleSheet("QLabel {padding: 0px 0px 35px 0px;}")

        self.UsernameTextBox = QLineEdit(self)
        self.UsernameTextBox.setMaximumWidth(700)
        self.UsernameTextBox.setMinimumWidth(500)

        self.StartLoginBtn  = QPushButton(self)
        self.ReturnToDashboard  = QPushButton(self)

        self.timer = QTimer()
        self.time = QTime(00, 00, 00)

        self.LoginLabelInfo.setText('Efetue seu login no Trakt!')
        self.LoginLabelInfo.setStyleSheet("QLabel {padding: 0px 0px 10px 0px;}")
        self.UsernameTextBox.setPlaceholderText('Insira seu usuario do Trakt.')

        self.StartLoginBtn.setText('Login')
        self.ReturnToDashboard.setText('Back')

        self.PrimaryVerticalLayout = QVBoxLayout()
        self.VerticalLayout = QHBoxLayout()
        self.HorizontalLayout = QHBoxLayout()
        self.LabelLayout = QHBoxLayout()
        self.LabelLayout1 = QHBoxLayout()

        self.LabelLayout.addStretch(1)
        self.LabelLayout.addWidget(self.LoginLabelInfo)
        self.LabelLayout.addStretch(1)

        self.LabelLayout1.addStretch(1)
        self.LabelLayout1.addWidget(self.StatusLabel)
        self.LabelLayout1.addStretch(1)
        
        self.PrimaryVerticalLayout.addStretch(3)
        self.VerticalLayout.addStretch(1)
        self.VerticalLayout.addWidget(self.UsernameTextBox)
        self.VerticalLayout.addStretch(1)
        self.HorizontalLayout.addStretch(1)
        self.HorizontalLayout.addWidget(self.StartLoginBtn)
        self.HorizontalLayout.addWidget(self.ReturnToDashboard)
        self.HorizontalLayout.addStretch(1)

        self.PrimaryVerticalLayout.addLayout(self.LabelLayout)
        self.PrimaryVerticalLayout.addLayout(self.LabelLayout1)
        # self.PrimaryVerticalLayout.addStretch(1)
        self.PrimaryVerticalLayout.addLayout(self.VerticalLayout)
        self.PrimaryVerticalLayout.addLayout(self.HorizontalLayout)
        self.PrimaryVerticalLayout.addStretch(3)
        self.setLayout(self.PrimaryVerticalLayout)

        self.StartLoginBtn.clicked.connect(self.MakeAuth)
        

    def MakeAuth(self):
        username = self.UsernameTextBox.text()

        if len(username) > 0:
            try:
                self.code = GetCode(username)
            except Exception as e:
                raise e

            if self.code.status_code == 200:
                self.code = json.loads(self.code.content)
                
                self.expires_in = self.code['expires_in']
                self.interval = self.code['interval']
                self.timer.start(self.expires_in * 1000)
                self.timer.setSingleShot(True)
                self.stop = True

                self.UpdateTimer() 
                self.doCheckAuth() 
                self.UsernameTextBox.setText(self.code['user_code'])                
                pass
            pass


        pass


    def UpdateTimer(self):
        if self.stop == True:
            self.time = self.time.addSecs(1)

            messege[1] = ''.join(['<a href=\"', self.code['verification_url'],'/\">', self.code['verification_url'], '</a>'])
            messege[4] = self.time.toString("hh:mm:ss")
            self.LoginLabelInfo.setText(''.join(messege))
            QTimer.singleShot(1000, self.UpdateTimer)
        else:
            self.LoginLabelInfo.setText('')
            pass
        pass


    def doCheckAuth(self):
        try:
            status = int(CheckAuth(self.code['device_code']))
        except Exception as e:
            raise e

        if status == 200:
            self.StatusLabel.setText('Login efetuado com Sucesso!')
            self.UsernameTextBox.setText('')
            self.stop = False
        elif status == 400:
            self.StatusLabel.setText('Aguardando aprovação!')
            self.stop = True
            QTimer.singleShot((self.interval * 1000), self.doCheckAuth) 
        elif status in [404, 409, 410, 418]:
            self.StatusLabel.setText('Houve um erro no Login!')
            self.stop = False
            pass

        pass