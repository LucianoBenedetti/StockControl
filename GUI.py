# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1501, 1003)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gBox_STOCK_DAY = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_STOCK_DAY.setEnabled(True)
        self.gBox_STOCK_DAY.setGeometry(QtCore.QRect(0, 0, 701, 631))
        self.gBox_STOCK_DAY.setObjectName("gBox_STOCK_DAY")
        self.scrollArea_FileList = QtWidgets.QScrollArea(self.gBox_STOCK_DAY)
        self.scrollArea_FileList.setGeometry(QtCore.QRect(30, 30, 321, 561))
        self.scrollArea_FileList.setWidgetResizable(True)
        self.scrollArea_FileList.setObjectName("scrollArea_FileList")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 319, 559))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_FileList.setWidget(self.scrollAreaWidgetContents)
        self.btn_Start_Stock_Day = QtWidgets.QPushButton(self.gBox_STOCK_DAY)
        self.btn_Start_Stock_Day.setGeometry(QtCore.QRect(380, 30, 301, 121))
        self.btn_Start_Stock_Day.setObjectName("btn_Start_Stock_Day")
        self.btn_COUNT_STOCK = QtWidgets.QPushButton(self.gBox_STOCK_DAY)
        self.btn_COUNT_STOCK.setGeometry(QtCore.QRect(380, 210, 301, 121))
        self.btn_COUNT_STOCK.setObjectName("btn_COUNT_STOCK")
        self.btn_delete_Files = QtWidgets.QPushButton(self.gBox_STOCK_DAY)
        self.btn_delete_Files.setGeometry(QtCore.QRect(380, 390, 301, 121))
        self.btn_delete_Files.setObjectName("btn_delete_Files")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(750, 0, 731, 921))
        self.groupBox.setObjectName("groupBox")
        self.btn_TRUCK_DAY = QtWidgets.QPushButton(self.groupBox)
        self.btn_TRUCK_DAY.setGeometry(QtCore.QRect(20, 30, 301, 121))
        self.btn_TRUCK_DAY.setObjectName("btn_TRUCK_DAY")
        self.btn_EXPIRED_DATES = QtWidgets.QPushButton(self.groupBox)
        self.btn_EXPIRED_DATES.setGeometry(QtCore.QRect(400, 30, 301, 121))
        self.btn_EXPIRED_DATES.setObjectName("btn_EXPIRED_DATES")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 180, 711, 711))
        self.calendarWidget.setObjectName("calendarWidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 690, 721, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_ADD_ITEM = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_ADD_ITEM.setGeometry(QtCore.QRect(20, 50, 301, 131))
        self.btn_ADD_ITEM.setObjectName("btn_ADD_ITEM")
        self.btn_CHECK_ITEM = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_CHECK_ITEM.setGeometry(QtCore.QRect(390, 50, 291, 131))
        self.btn_CHECK_ITEM.setObjectName("btn_CHECK_ITEM")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1501, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gBox_STOCK_DAY.setTitle(_translate("MainWindow", "STOCK DAY"))
        self.btn_Start_Stock_Day.setText(_translate("MainWindow", "STOCK DAY"))
        self.btn_COUNT_STOCK.setText(_translate("MainWindow", "COUNT STOCK"))
        self.btn_delete_Files.setText(_translate("MainWindow", "Delete Files"))
        self.groupBox.setTitle(_translate("MainWindow", "TRUCK DAY"))
        self.btn_TRUCK_DAY.setText(_translate("MainWindow", "TRUCK DAY"))
        self.btn_EXPIRED_DATES.setText(_translate("MainWindow", "EXIPRED DATES"))
        self.groupBox_2.setTitle(_translate("MainWindow", "DATA BASE"))
        self.btn_ADD_ITEM.setText(_translate("MainWindow", "ADD ITEM"))
        self.btn_CHECK_ITEM.setText(_translate("MainWindow", "CHECK ITEM"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




