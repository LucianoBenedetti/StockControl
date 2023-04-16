import pyperclip as pc
import pandas as pd
import threading
from datetime import date 



def SaveDataExpire():
    dataExpire.to_csv('ExpireDates.DB', header=True, index=False)
    #print("\nSe guardo")
    event = threading.Timer(20, SaveDataExpire)    #Autosave de DataBase
    event.start()



def UpdateExpireDates(barcode):
    
    ##### --------------------------BUSCO ITEM EN BASE DE DATOS-----------------------------
    if dataBase[ dataBase['BARCODE']==barcode].empty:  # si no existe, no esta en la base de datos
        print("The Item no Exist on Data Base, Updtate data Base First")

    else:                                              #existe, remplazon por nombre de producto
        producto=dataBase[ dataBase['BARCODE']==barcode]
        producto=producto['ITEMS'].values[0]

        Dates=input(f"{barcode} --> {producto} When Expired? (DD/MM/YY): ")
        Dates=Dates.split('/')
        Dates=date( (int(Dates[2])+2000) , int(Dates[1]) , int(Dates[0]) )
        print(Dates)
        chose=input(f"Do you want ADD {barcode} --> {producto} expired on {Dates}?  (Y/N):  ")
        if chose.upper() == 'Y':
            dataExpire.loc[len(dataExpire.index)] = [Dates,producto]   #agrea nueva producto a la base   #actualizo base de datos a lista
            print (f"{producto}   {Dates}")


dataBase =  pd.read_csv('DataBase.DB')
dataExpire = pd.read_csv('ExpireDates.DB')

pc.copy('') #Limpio Clipboard

event = threading.Timer(20, SaveDataExpire)    #Autosave de DataBase
event.start()

print("\n\nProgram to Uptate DATABASE file, response for each answer Y or N and for end press CTRL + C\nStart to SCAN ITEMS...\n\n")

try:
    while True:
        if pc.waitForPaste():   #Nuevo barcode detectado
            barcode=int(pc.paste())
            pc.copy('')         #Limpio Clipboard
            UpdateExpireDates(barcode)
            
        print("\n SCAN NEXT ITEM or press CTRL + C to exit...") 
except KeyboardInterrupt:           #Si preciono CTRL + C salgo y guardo base de datos
    pass
    print("\n \n END OF PROGRAM ")
    dataExpire.to_csv('ExpireDates.DB', header=True, index=False)
    #cancelo evento timer
    threads= threading.enumerate()
    for thr in threads:
        try:
            thr.cancel()
        except:
            pass