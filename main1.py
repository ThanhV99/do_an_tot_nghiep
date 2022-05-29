# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dg2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot

import cv2
from src.model import Model


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1233, 983)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.gridLayout_10.addWidget(self.label_title, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_control = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_control.sizePolicy().hasHeightForWidth())
        self.groupBox_control.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_control.setFont(font)
        self.groupBox_control.setObjectName("groupBox_control")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_control)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_control)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_control, 1, 1, 1, 1)
        self.groupBox_text_result = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_text_result.sizePolicy().hasHeightForWidth())
        self.groupBox_text_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_text_result.setFont(font)
        self.groupBox_text_result.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_text_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_text_result.setFlat(False)
        self.groupBox_text_result.setCheckable(False)
        self.groupBox_text_result.setObjectName("groupBox_text_result")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_text_result)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_result1 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result1.setFont(font)
        self.label_result1.setObjectName("label_result1")
        self.gridLayout.addWidget(self.label_result1, 0, 0, 1, 1)
        self.label_count1 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_count1.setFont(font)
        self.label_count1.setObjectName("label_count1")
        self.gridLayout.addWidget(self.label_count1, 0, 1, 1, 1)
        self.label_result2 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result2.setFont(font)
        self.label_result2.setObjectName("label_result2")
        self.gridLayout.addWidget(self.label_result2, 1, 0, 1, 1)
        self.label_count2 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_count2.setFont(font)
        self.label_count2.setObjectName("label_count2")
        self.gridLayout.addWidget(self.label_count2, 1, 1, 1, 1)
        self.label_result3 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result3.setFont(font)
        self.label_result3.setObjectName("label_result3")
        self.gridLayout.addWidget(self.label_result3, 2, 0, 1, 1)
        self.label_count3 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_count3.setFont(font)
        self.label_count3.setObjectName("label_count3")
        self.gridLayout.addWidget(self.label_count3, 2, 1, 1, 1)
        self.label_result4 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result4.setFont(font)
        self.label_result4.setObjectName("label_result4")
        self.gridLayout.addWidget(self.label_result4, 3, 0, 1, 1)
        self.label_count4 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_count4.setFont(font)
        self.label_count4.setObjectName("label_count4")
        self.gridLayout.addWidget(self.label_count4, 3, 1, 1, 1)
        self.label_result5 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result5.setFont(font)
        self.label_result5.setObjectName("label_result5")
        self.gridLayout.addWidget(self.label_result5, 4, 0, 1, 1)
        self.label_count5 = QtWidgets.QLabel(self.groupBox_text_result)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_count5.setFont(font)
        self.label_count5.setObjectName("label_count5")
        self.gridLayout.addWidget(self.label_count5, 4, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_text_result, 1, 0, 1, 1)
        self.groupBox_cam_result = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_cam_result.setMinimumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_cam_result.setFont(font)
        self.groupBox_cam_result.setObjectName("groupBox_cam_result")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_cam_result)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_result = QtWidgets.QLabel(self.groupBox_cam_result)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.gridLayout_8.addWidget(self.label_result, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_cam_result, 0, 1, 1, 1)
        self.groupBox_cam = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_cam.sizePolicy().hasHeightForWidth())
        self.groupBox_cam.setSizePolicy(sizePolicy)
        self.groupBox_cam.setMinimumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_cam.setFont(font)
        self.groupBox_cam.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_cam.setObjectName("groupBox_cam")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_cam)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_camera = QtWidgets.QLabel(self.groupBox_cam)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_camera.sizePolicy().hasHeightForWidth())
        self.label_camera.setSizePolicy(sizePolicy)
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.gridLayout_7.addWidget(self.label_camera, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_cam, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1233, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
        # nut an chup man hinh
        self.pushButton.clicked.connect(self.capture_image)
        self.red_apples = 0
        self.green_apples = 0
        self.rotten_apples = 0

    # chup man hinh
    def capture_image(self):
        # xu ly
        img = self.thread.img
        detections = model.pre_process(img)
        result_img, red_apples, green_apples, rotten_apples = model.post_process(img.copy(), detections)
        # so luong
        self.red_apples += red_apples
        self.green_apples += green_apples
        self.rotten_apples += rotten_apples
        self.update_text_result()
        # detect kich thuoc

        # ve len man hinh 2
        qt_img = self.convert_cv_qt(result_img)
        self.label_result.setPixmap(qt_img)

    # update ket qua
    def update_text_result(self):
        self.label_count1.setText(str(self.red_apples))
        self.label_count3.setText(str(self.green_apples))
        self.label_count5.setText(str(self.rotten_apples))

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

        # @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.label_camera.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        w_label, h_label = self.label_camera.width(), self.label_camera.height()
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(w_label, h_label, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Đại học Bách Khoa Hà Nội"))
        self.groupBox_control.setTitle(_translate("MainWindow", "Bảng điều khiển"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.pushButton_3.setText(_translate("MainWindow", "RESET"))
        self.groupBox_text_result.setTitle(_translate("MainWindow", "Kết quả"))
        self.label_result1.setText(_translate("MainWindow", "Táo đỏ to:"))
        self.label_count1.setText(_translate("MainWindow", "0"))
        self.label_result2.setText(_translate("MainWindow", "Táo đỏ nhỏ:"))
        self.label_count2.setText(_translate("MainWindow", "0"))
        self.label_result3.setText(_translate("MainWindow", "Táo xanh to:"))
        self.label_count3.setText(_translate("MainWindow", "0"))
        self.label_result4.setText(_translate("MainWindow", "Táo xanh nhỏ:"))
        self.label_count4.setText(_translate("MainWindow", "0"))
        self.label_result5.setText(_translate("MainWindow", "Táo hỏng:"))
        self.label_count5.setText(_translate("MainWindow", "0"))
        self.groupBox_cam_result.setTitle(_translate("MainWindow", "Kết quả detect"))
        self.groupBox_cam.setTitle(_translate("MainWindow", "Camera"))


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            self.img = cv_img
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()

if __name__ == "__main__":
    import sys
    # load model
    print("start model")
    model = Model("weights/last.onnx")

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
