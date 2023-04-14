from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess

from GUI import Ui_MainWindow



def Stock_Day():
    l=subprocess.run(["C:\Program Files (x86)\Barcode2Win\Barcode2win.exe"])
def Count_Stock():
    l=subprocess.run(["COUNT_STOCK.bat"])


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


ui.btn_Start_Stock_Day.clicked.connect(Stock_Day)
ui.btn_COUNT_STOCK.clicked.connect(Count_Stock)
MainWindow.show()
sys.exit(app.exec_())