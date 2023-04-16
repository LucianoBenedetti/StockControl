from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import subprocess
import glob # list files on folder
import threading
import pandas as pd
from datetime import date 
import openpyxl #excel
import time

from GUI import Ui_MainWindow


#----------PATHS------------#
Barcode2Win="C:\Program Files (x86)\Barcode2Win\Barcode2win.exe"
#To convert ui to py
# pyuic5 -x GUI.ui -o GUI.py


#list widget    
def FileList():
    file_list = glob.glob("*.csv")
    ui.list_FileList.clear()
    for file in file_list:
        ui.list_FileList.addItem(file)


def LockButton():
    ui.btn_ADD_ITEM.setEnabled(False)
    ui.btn_Start_Stock_Day.setEnabled(False)
    ui.btn_COUNT_STOCK.setEnabled(False)
    ui.btn_delete_Files.setEnabled(False)
    ui.btn_CHECK_ITEM.setEnabled(False)
    ui.btn_TRUCK_DAY.setEnabled(False)
    ui.btn_EXPIRED_DATES.setEnabled(False)

def UnlockButton():
    ui.btn_ADD_ITEM.setEnabled(True)
    ui.btn_Start_Stock_Day.setEnabled(True)
    ui.btn_COUNT_STOCK.setEnabled(True)
    ui.btn_delete_Files.setEnabled(True)
    ui.btn_CHECK_ITEM.setEnabled(True)
    ui.btn_TRUCK_DAY.setEnabled(True)
    ui.btn_EXPIRED_DATES.setEnabled(True)

# BOTOMS EVENTS
def Stock_Day():
    LockButton()
    app=subprocess.Popen([Barcode2Win])
    try:
        cmd=subprocess.run(["python","DisplayScann.py"])
    except KeyboardInterrupt:           #Si preciono CTRL + C salgo
        pass
    app.kill()
    UnlockButton()

def Count_Stock():
    #cmd=subprocess.run(["COUNT_STOCK.bat"])
    cmd=subprocess.Popen(["python","CountStock.py"])
    time.sleep(5)
    app=subprocess.Popen(["start","EXCEL","STOCK.xlsx"],shell=True)

def Delete_Files():
    cmd=subprocess.Popen(["del","*.csv"],shell=True)
    ui.list_FileList.clear()

def AddItem():
    LockButton()
    app=subprocess.Popen([Barcode2Win])
    try:
        cmd=subprocess.run(["python","ADDItemsToDataBase.py"])
    except KeyboardInterrupt:           #Si preciono CTRL + C salgo
        pass
    app.kill()
    UnlockButton()

def CheckItems():
    LockButton()
    app=subprocess.Popen([Barcode2Win])
    try:
        cmd=subprocess.run(["python","DataBaseCheckItems.py"])
    except KeyboardInterrupt:           #Si preciono CTRL + C salgo
        pass
    app.kill()
    UnlockButton()

def TruckDay():
    LockButton()
    app=subprocess.Popen([Barcode2Win])
    try:
        cmd=subprocess.run(["python","TruckDay.py"])
    except KeyboardInterrupt:           #Si preciono CTRL + C salgo
        pass
    app.kill()
    UnlockButton()
    dataExpire = pd.read_csv('ExpireDates.DB')
    LoadCalendary(dataExpire)


#----------CalendarWidget---------------#
def MarkDate(Date):
    # format
    format = QTextCharFormat()
    format.setFont(QFont('Times', 15))
    format.setForeground(Qt.green)
   
    # setting date text format
    ui.calendarWidget.setDateTextFormat(Date, format)

def LoadCalendary(dataExpire):
    for index, row in dataExpire.iterrows():
        Date=date.fromisoformat(row[0])
        #print(Date)
        MarkDate(QDate(Date))

def ShowProduct():
    dataExpire = pd.read_csv('ExpireDates.DB')
    Date_obj = ui.calendarWidget.selectedDate()
    Date_obj=Date_obj.toPyDate()
    Date=date.isoformat(Date_obj)
    
    #print(Date)
    ##### --------------------------BUSCO ITEM EN BASE DE DATOS-----------------------------
    if dataExpire[ dataExpire['DATE']==Date].empty:     # si no existe, no esta en la base de datos
        ui.lbl_Calendary.setText("")
    else:                                               #existe, remplazon por nombre de producto
        producto=dataExpire[ dataExpire['DATE']==Date]
        #print("\n".join(producto['ITEMS'].values))
        ui.lbl_Calendary.setText( "\n".join(producto['ITEMS'].values))

#Create Excel
def ExpiredDates():
    dataExpire.to_excel("ExpireDates.xlsx",sheet_name="ExpireDates")
    app=subprocess.Popen(["start","EXCEL","ExpireDates.xlsx"],shell=True)


#---------------GUI Init----------------#
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

dataExpire = pd.read_csv('ExpireDates.DB')


ui.btn_Start_Stock_Day.clicked.connect(Stock_Day)
ui.btn_COUNT_STOCK.clicked.connect(Count_Stock)
ui.btn_delete_Files.clicked.connect(Delete_Files)

ui.btn_ADD_ITEM.clicked.connect(AddItem)
ui.btn_CHECK_ITEM.clicked.connect(CheckItems)

ui.btn_TRUCK_DAY.clicked.connect(TruckDay)
ui.calendarWidget.clicked.connect(ShowProduct)
# making it multi line
ui.lbl_Calendary.setWordWrap(True)
ui.btn_EXPIRED_DATES.clicked.connect(ExpiredDates)

MainWindow.show()

#---------Funcion Init---------#
FileList()
LoadCalendary(dataExpire)

#----------Thread Main---------#
def Main():
    FileList()
    
    event = threading.Timer(5, Main)    
    event.start()
    #print(f"Entro {threading.enumerate()}")

event = threading.Timer(5, Main)    
event.start()

#print(f"Paso {threading.enumerate()}")


#-------------END APP ------------#
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
