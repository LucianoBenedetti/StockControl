import pyperclip as pc
import pandas as pd
import threading

End_main = False

def SaveDataBase():
    dataBase.to_csv('DataBase.DB', header=True, index=False)
    #print("\nSe guardo")
    if End_main == False:
        event = threading.Timer(20, SaveDataBase)    #Autosave de DataBase
        event.start()



def UpdateDataBase(barcode):
    carton='UNIT'
    ##### --------------------------BUSCO ITEM EN BASE DE DATOS-----------------------------
    if dataBase[ dataBase['BARCODE']==barcode].empty:  # si no existe, no esta en la base de datos
        producto=input(f"Name of new product  {barcode}: ").upper()
        
        chose=input(f"Is {producto} CARTON?")           #unidad simple o paquete
        if chose.upper() == 'Y':
            carton='CTN'

        chose=input(f"Add to DataBase {barcode} --> {producto} --> {carton}?")
        if chose.upper() == 'Y':
            dataBase.loc[len(dataBase.index)] = [barcode, producto, carton]   #agrea nueva producto a la base

    else:                                              #existe, remplazon por nombre de producto
        producto=dataBase[ dataBase['BARCODE']==barcode]
        
        chose=input(f"{barcode} --> {producto['ITEMS'].values[0]} are exist, Do you want to change with other product name?")
        if chose.upper() == 'Y':
            chose=input(f"Is {producto['ITEMS'].values[0]} CARTON?")           #unidad simple o paquete
            if chose.upper() == 'Y':
                carton='CTN'
            producto=input(f"NEW Name of product of {barcode}: ").upper()
            dataBase.loc[dataBase['BARCODE']==barcode] = [barcode,  producto, carton]   #actualizo base de datos a lista

    return dataBase[ dataBase['BARCODE']==barcode] 


dataBase =  pd.read_csv('DataBase.DB')
pc.copy('') #Limpio Clipboard

event = threading.Timer(20, SaveDataBase)    #Autosave de DataBase
event.start()

print("\n\nProgram to Uptate DATABASE file, response for each answer Y or N and for end press CTRL + C\nStart to SCAN ITEMS...\n\n")

try:
    while True:
        if pc.waitForPaste():   #Nuevo barcode detectado
            barcode=int(pc.paste())
            pc.copy('')         #Limpio Clipboard
            row=UpdateDataBase(barcode)
            print(row)
        print("\n SCAN NEXT ITEM or press CTRL + C to exit...") 
except KeyboardInterrupt:           #Si preciono CTRL + C salgo y guardo base de datos
    pass
    print("\n \n END OF PROGRAM ")
    End_main = True
    dataBase.to_csv('DataBase.DB', header=True, index=False)