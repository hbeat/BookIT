from PyQt5 import QtCore, QtGui, QtWidgets
import ZODB, ZODB.FileStorage, persistent, BTrees.OOBTree, transaction
from user import User
class Ui_Register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(120, 70, 171, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 71, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_firstname = QtWidgets.QLineEdit(Form)
        self.lineEdit_firstname.setGeometry(QtCore.QRect(120, 100, 171, 22))
        self.lineEdit_firstname.setObjectName("lineEdit_firstname")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_lastname = QtWidgets.QLineEdit(Form)
        self.lineEdit_lastname.setGeometry(QtCore.QRect(120, 130, 171, 22))
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 160, 71, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 160, 171, 22))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 190, 151, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(Form)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(160, 190, 131, 22))
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.registerBtn = QtWidgets.QPushButton(Form)
        self.registerBtn.setGeometry(QtCore.QRect(140, 240, 93, 28))
        self.registerBtn.setObjectName("registerBtn")
##We add
        self.registerBtn.clicked.connect(lambda:self.register(Form))
##We add
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BookIt"))
        self.label.setText(_translate("Form", "Register"))
        self.label_3.setText(_translate("Form", "Email:"))
        self.label_4.setText(_translate("Form", "First name:"))
        self.label_5.setText(_translate("Form", "Last name:"))
        self.label_6.setText(_translate("Form", "Password:"))
        self.label_7.setText(_translate("Form", "Confirm Password:"))
        self.registerBtn.setText(_translate("Form", "Register"))

    def register(self,Form):
        if self.lineEdit_password.text() != self.lineEdit_confirm_password.text():
            print("Incorrect password")
            return
        email = self.lineEdit_email.text()
        first_name = self.lineEdit_firstname.text()
        last_name = self.lineEdit_lastname.text()
        password = self.lineEdit_password.text()
        user = User(email,first_name,last_name,password)

        #connect and link to ZODB database
        storage = ZODB.FileStorage.FileStorage('userDB.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root()
        root[email] = user
        transaction.commit()
        connection.close()
        db.close()
        print("register complete") ##do something such as transition into login ui
        Form.close()


if __name__ == "__main__":
    import sys
    # storage = ZODB.FileStorage.FileStorage('userDB.fs')
    # db = ZODB.DB(storage)
    # connection = db.open()
    # root = connection.root()
    # for k,v in root.items():
    #     print(k,v)
    # connection.close()
    # db.close()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
