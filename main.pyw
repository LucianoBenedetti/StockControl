from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import glob # list files on folder
import threading

from GUI import Ui_MainWindow

#To convert ui to py
# pyuic5 -x GUI.ui -o GUI.py


def Stock_Day():
    l=subprocess.run(["C:\Program Files (x86)\Barcode2Win\Barcode2win.exe"])
def Count_Stock():
    l=subprocess.run(["COUNT_STOCK.bat"])
def AddItem():
    l=subprocess.Popen(["C:\Program Files (x86)\Barcode2Win\Barcode2win.exe"])
    l=subprocess.Popen(["python","ADDItemsToDataBase.py"])
    ui.btn_ADD_ITEM.setEnabled(False)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


ui.btn_Start_Stock_Day.clicked.connect(Stock_Day)
ui.btn_COUNT_STOCK.clicked.connect(Count_Stock)
ui.btn_ADD_ITEM.clicked.connect(AddItem)

MainWindow.show()


#look files CSV
file_list = glob.glob("*.csv")
ui.list_FileList.clear()
for file in file_list:
    ui.list_FileList.addItem(file)



#----------Thread Main---------#
def Main():
    file_list = glob.glob("*.csv")
    print(f"Entro {threading.enumerate()}")
    ui.list_FileList.clear()
    for file in file_list:
        ui.list_FileList.addItem(file)
    event = threading.Timer(5, Main)    
    event.start()

event = threading.Timer(5, Main)    
event.start()

#print(f"Paso {threading.enumerate()}")

#When close app, cancel Thread Main
if app.exec_() == 0:
   
    threads= threading.enumerate()
    for thr in threads:
        try:
            thr.cancel()
        except:
            pass
    
    #print(f"Salio: {threading.enumerate()}")
    sys.exit()
