import ZODB, ZODB.FileStorage, persistent, BTrees.OOBTree, transaction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from register_window import Ui_Register
from os import environ
import user
# environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
#------------------------------------------------
class QLabelClickable(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(QLabelClickable,self).__init__(parent)
    def mousePressEvent(self,event):
        self.action = "click"
    def mouseReleaseEvent(self,event):
        if self.action == "click":
            self.clicked.emit(self.action)
#--------------------------------------------------
class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(130, 70, 141, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(130, 110, 141, 22))
        self.lineEdit_password.setObjectName("lineEdit_password")

##We add        
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
##We add
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(130, 150, 81, 28))
        self.login_btn.setObjectName("login_btn")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 210, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_register = QLabelClickable(Form)
        self.label_register.setGeometry(QtCore.QRect(200, 210, 55, 16))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_register.setFont(font)
        self.label_register.setObjectName("label_register")
        self.label_register.setStyleSheet('QLabel {color: blue;}')
        self.label_register.setCursor(QCursor(Qt.PointingHandCursor))
##We add
        self.login_btn.clicked.connect(self.login_clicked)
        self.label_register.clicked.connect(self.open_register)
##We add       
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BookIt"))
        self.label.setText(_translate("Form", "Log in"))
        self.label_2.setText(_translate("Form", "email:"))
        self.label_3.setText(_translate("Form", "password:"))
        self.login_btn.setText(_translate("Form", "Log in"))
        self.label_4.setText(_translate("Form", "Not member?"))
        self.label_register.setText(_translate("Form", "Register"))

#we add
    def login_clicked(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()

        storage = ZODB.FileStorage.FileStorage('userDB.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()
        for k,v in root.items():
            if k == email:
                if password == v.get_password():
                    print("login success")
                    connection.close()
                    db.close()
                    #transition to login page
                    return
                else:
                    continue
        print("Not correct password")
        connection.close()
        db.close()

    def open_register(self):
        self.register_form = QtWidgets.QWidget()
        self.register_ui = Ui_Register()
        self.register_ui.setupUi(self.register_form)
        self.register_form.show()

##ZODB
# storage = ZODB.FileStorage.FileStorage('testDB.fs')
# db = ZODB.DB(storage)
# connection = db.open()
# root = connection.root()

# connection.close()
# db.close()

if __name__ == "__main__":
    import sys
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
