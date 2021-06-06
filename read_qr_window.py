from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from read_qr_ui import Ui_Read_QR
import cv2
import sys

class ReadQR(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Read_QR()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.scan_btn.clicked.connect(self.controlTimer)
        self.ui.cancel_btn.clicked.connect(self.stopTimer)

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        #decode the qrcode
        data, bbox, _ = self.detector.detectAndDecode(image)
        #check if there is a QRCode in the image
 #----------------------------------       
        if data:
            print("QR decode: ",data)
            #for booking key in bookindata:
            #   if data==booking key and timein<datetimenow<timeout:
            #       login success
            ##continue do something after decode QR
#-----------------------------------
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
        
    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # create QRCode detector
            self.detector = cv2.QRCodeDetector()
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.scan_btn.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.image_label.clear()
            self.ui.scan_btn.setText("Start")

    def stopTimer(self):
        try:
            self.cap.release()
        except:
            print("Error")
        self.timer.stop()
        self.ui.image_label.clear()
        #exit and return to mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = ReadQR()
    mainWindow.show()

    sys.exit(app.exec_())
