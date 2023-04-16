import pyperclip as pc
import pandas as pd

dataBase =  pd.read_csv('DataBase.DB')

pc.copy('') #Limpio Clipboard

print("\n\nProgram to Check DATABASE file, for end press CTRL + C\nStart to SCAN ITEMS...\n\n")

try:
    while True:
        if pc.waitForPaste():   #Nuevo barcode detectado
            barcode=int(pc.paste())
            pc.copy('')         #Limpio Clipboard
            
            if dataBase[ dataBase['BARCODE']==barcode].empty:  # si no existe, no esta en la base de datos
                print("That item no Exist in BaseDate")
            else:                                              #existe, remplazon por nombre de producto
                print(dataBase[ dataBase['BARCODE']==barcode])

        print("\n SCAN NEXT ITEM or press CTRL + C to exit...") 
except KeyboardInterrupt:           #Si preciono CTRL + C salgo y guardo base de datos
    pass
    print("\n \n END OF PROGRAM ")
