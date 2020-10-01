from PyQt5.QtWidgets import QPushButton, QWidget
# 

class LoginUI(QWidget):
    def __init__(self, parent=None):
        super(LoginUI, self).__init__(parent)
        self.BackBtn = QPushButton('Back', self)
        self.BackBtn.move(100, 350)


